import math, numpy, matplotlib
import matplotlib.pyplot as plt

def triangular_lattice(point_distance ,expansion_level = 4, starting_point = (0, 0)):

    set_of_points_on_the_plane = set()

    for current_level in range(expansion_level+1):

        temporary_hexagon_coordinates = {}

        equilateral_triangle_side = current_level * point_distance
        equilateral_triangle__half_side = equilateral_triangle_side / 2
        equilateral_triangle_height = (math.sqrt(3) * equilateral_triangle_side) / 2
        if current_level != 0:
            point_distance_as_triangle_side_percentage = point_distance / equilateral_triangle_side

        temporary_hexagon_coordinates['right'] = (starting_point[0] + point_distance * current_level, starting_point[1]) #right
        temporary_hexagon_coordinates['left'] = (starting_point[0] - point_distance * current_level, starting_point[1]) #left
        temporary_hexagon_coordinates['top_right'] = (starting_point[0] + equilateral_triangle__half_side, starting_point[1] + equilateral_triangle_height) #  top_right
        temporary_hexagon_coordinates['top_left'] = (starting_point[0] - equilateral_triangle__half_side, starting_point[1] + equilateral_triangle_height) #  top_left
        temporary_hexagon_coordinates['bottom_right'] = (starting_point[0] + equilateral_triangle__half_side, starting_point[1] - equilateral_triangle_height) #  bottom_right
        temporary_hexagon_coordinates['bottom_left'] = (starting_point[0] - equilateral_triangle__half_side, starting_point[1] - equilateral_triangle_height) # bottom_left

        if current_level > 1:
            for intermediate_points in range(1, current_level):

                set_of_points_on_the_plane.add( (temporary_hexagon_coordinates['left'][0] + intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['top_left'][0] - temporary_hexagon_coordinates['left'][0]) , temporary_hexagon_coordinates['left'][1] + intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['top_left'][1] - temporary_hexagon_coordinates['left'][1])  ))        #from left to top left
                print(intermediate_points)
                print((temporary_hexagon_coordinates['left'][0] + intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['top_left'][0] - temporary_hexagon_coordinates['left'][0]) , temporary_hexagon_coordinates['left'][1] + intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['top_left'][1] - temporary_hexagon_coordinates['left'][1])  ))
                set_of_points_on_the_plane.add( (temporary_hexagon_coordinates['left'][0] + intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['bottom_left'][0] - temporary_hexagon_coordinates['left'][0]) , temporary_hexagon_coordinates['left'][1] - intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['bottom_left'][1] - temporary_hexagon_coordinates['left'][1]) ))  # from left to bottom left

                set_of_points_on_the_plane.add( (temporary_hexagon_coordinates['top_right'][0] - intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['top_left'][0] - temporary_hexagon_coordinates['top_right'][0]) , temporary_hexagon_coordinates['top_right'][1] ))  #from top right to top left
                set_of_points_on_the_plane.add( (temporary_hexagon_coordinates['top_right'][0] + intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['right'][0] - temporary_hexagon_coordinates['top_right'][0]) , temporary_hexagon_coordinates['top_left'][1] - intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['right'][1] - temporary_hexagon_coordinates['top_right'][1]) ))    # from top right to right

                set_of_points_on_the_plane.add( (temporary_hexagon_coordinates['bottom_right'][0] - intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['bottom_left'][0] - temporary_hexagon_coordinates['bottom_right'][0]) , temporary_hexagon_coordinates['bottom_right'][1] ))   #apo bottom right pros aristera
                set_of_points_on_the_plane.add( (temporary_hexagon_coordinates['bottom_right'][0] + intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['right'][0] - temporary_hexagon_coordinates['bottom_right'][0]) , temporary_hexagon_coordinates['bottom_right'][1] + intermediate_points * point_distance_as_triangle_side_percentage * abs(temporary_hexagon_coordinates['right'][1] - temporary_hexagon_coordinates['bottom_right'][1]) ))         # from bottom right to right

        # dictionary to set

        set_of_points_on_the_plane.update( temporary_hexagon_coordinates.values() )

    return list(set_of_points_on_the_plane)
