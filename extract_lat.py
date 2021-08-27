
from skimage.feature import peak_local_max
import re
import linecache
import numpy as np
from scipy.spatial import KDTree

def lat_con(topofile='Data/18d03T0015.txt',thrs=0.2,pxdist=3):
    data=np.loadtxt(topofile)
    data_z=data*1e9
    xy = peak_local_max(data_z, min_distance=pxdist,threshold_abs=thrs)
    tree=KDTree(xy)
    dd,ii=tree.query(xy,k=2)
    a,b=np.histogram(dd[:,1],bins=30)
    c=b[np.where(a==max(a))][0]
    imsize= [float(x.strip(' "')) for x in re.findall("\d+\.\d+", linecache.getline(topofile, 2))][0]
    pxsize=imsize/data_z.shape[0]
    latcon=c*pxsize
    data_x=np.linspace(0, imsize, num=data_z.shape[0])
    data_y=data_x
    X,Y=np.meshgrid(data_x,data_y)
    xynm=xy*pxsize
    return latcon, X,Y,data_z, xynm
