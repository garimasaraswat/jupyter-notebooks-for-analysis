# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------
# Set up lattice
lattice = Hexagonal(4.138*Angstrom, 48.64*Angstrom)

# Define elements
elements = [Selenium, Bismuth, Selenium, Bismuth, Selenium, Selenium, Bismuth,
            Selenium, Bismuth, Selenium, Selenium, Bismuth, Selenium, Bismuth,
            Selenium]

# Define coordinates
fractional_coordinates = [[ 0.33333333    ,  0.66666666    ,  0.251912282664],
                          [ 0.66666667    ,  0.33333334    ,  0.288222585757],
                          [ 0.            ,  0.            ,  0.326888157895],
                          [ 0.33333333    ,  0.66666666    ,  0.365553730033],
                          [ 0.66666667    ,  0.33333334    ,  0.401864033125],
                          [ 0.            ,  0.            ,  0.448184210526],
                          [ 0.33333333    ,  0.66666666    ,  0.484494519507],
                          [ 0.66666667    ,  0.33333334    ,  0.523160085757],
                          [ 0.            ,  0.            ,  0.561825657895],
                          [ 0.33333333    ,  0.66666666    ,  0.598135966875],
                          [ 0.66666667    ,  0.33333334    ,  0.644456138388],
                          [ 0.            ,  0.            ,  0.680766447368],
                          [ 0.33333333    ,  0.66666666    ,  0.719432019507],
                          [ 0.66666667    ,  0.33333334    ,  0.758097585757],
                          [ 0.            ,  0.            ,  0.794407894737]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
#----------------------------------------
# Basis Set
#----------------------------------------
SeleniumBasis = OpenMXBasisSet(
    element=PeriodicTable.Selenium,
    filename="openmx/pao/Se7.0.pao.zip",
    atomic_species="s2p2d1",
    pseudopotential=NormConservingPseudoPotential("normconserving/upf2/Se_PBE13.upf.zip"),
    )


BismuthBasis = OpenMXBasisSet(
    element=PeriodicTable.Bismuth,
    filename="openmx/pao/Bi8.0.pao.zip",
    atomic_species="s2p2d2f1",
    pseudopotential=NormConservingPseudoPotential("normconserving/upf2/Bi_PBE13.upf.zip"),
    )

basis_set = [
    SeleniumBasis,
    BismuthBasis,
    ]

#----------------------------------------
# Exchange-Correlation
#----------------------------------------
exchange_correlation = GGA.PBE

numerical_accuracy_parameters = NumericalAccuracyParameters(
    electron_temperature=50.0*Kelvin,
    k_point_sampling=(9, 9, 1),
    density_mesh_cutoff=150.0*Hartree,
    )

calculator = LCAOCalculator(
    basis_set=basis_set,
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    )

bulk_configuration.setCalculator(calculator)

# -------------------------------------------------------------
# GGA Initial State
# -------------------------------------------------------------
MemoryUsage(bulk_configuration)
bulk_configuration.update()
nlsave('Bi2Se3_slab.nc', bulk_configuration)
nlprint(bulk_configuration)

# -------------------------------------------------------------
# Modify GGA calculator settings for SOGGA
# -------------------------------------------------------------
iteration_control_parameters = IterationControlParameters(
    algorithm=PulayMixer(noncollinear_mixing=True),
    )
calculator = bulk_configuration.calculator()
calculator = calculator(
    exchange_correlation=SOGGA.PBE,
    iteration_control_parameters=iteration_control_parameters,
    )

# -------------------------------------------------------------
# Initial State
# -------------------------------------------------------------
initial_spin = InitialSpin(scaled_spins=[0.0]*len(bulk_configuration))
bulk_configuration.setCalculator(
    calculator,
    initial_spin=initial_spin,
    initial_state=bulk_configuration
    )
MemoryUsage(bulk_configuration)
bulk_configuration.update()
nlsave('Bi2Se3_slab.nc', bulk_configuration)
nlprint(bulk_configuration)

# -------------------------------------------------------------
# Bandstructure
# -------------------------------------------------------------
bandstructure = Bandstructure(
    configuration=bulk_configuration,
    route=['K', 'G', 'M'],
    points_per_segment=201,
    bands_above_fermi_level=All
    )
nlsave('Bi2Se3_slab.nc', bandstructure)
