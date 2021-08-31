
from skimage.feature import peak_local_max
import re
import linecache
import numpy as np
from scipy.spatial import KDTree

def lat_con(topofile='Data/18d03T0015.txt',thrs=0.2,pxdist=3):
    data=np.loadtxt(topofile)
    data_z=data/np.mean(data)
    xy = peak_local_max(data_z, min_distance=pxdist,threshold_abs=thrs)
    tree=KDTree(xy)
    dd,ii=tree.query(xy,k=4)
    #a,b=np.histogram(dd[:,1],bins=30)
    #c=b[np.where(a==max(a))][0]
    imsize= [float(x.strip(' "')) for x in re.findall("\d+\.\d+", linecache.getline(topofile, 2))][0]
    pxsize=imsize/data_z.shape[0]
    nn1=dd[:,1]*pxsize
    nn2=dd[:,2]*pxsize
    nn3=dd[:,3]*pxsize
    data_x=np.linspace(0, imsize, num=data_z.shape[0])
    data_y=data_x
    X,Y=np.meshgrid(data_x,data_y)
    xynm=xy*pxsize
    return nn1,nn2,nn3, X,Y,data_z, xynm
