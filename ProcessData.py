import h5py
import os
import numpy as np


def loaddata(filepath, key = None, is3D = False, shape = (240, 240, 256)):
    file = h5py.File(filepath, "r")
    
    if is3D == True:
        print "loading 3D file: ", filepath
        d3dc = file["images3D/C"]
        d3dv = file["images3D/V"]
        retc = []
        for i, x  in enumerate(d3dc):
            retc.append(np.histogramdd(x, bins=shape, weights=d3dv[i])[0])

        return retc

    else:
        print "loading 2D file: ", filepath
        if key != None:
            return file[key], file

        return file


def loaddata3d(filepath):
    print "loading: ", filepath


def savedata(dgroup, fulldata, sdata, skey, outputpath, filename):
    print " saving: ", outputpath + filename
    savefile = h5py.File(outputpath + filename, 'w')
    for k in fulldata.keys():
        if k == skey:
            data = sdata
        else:
            data = fulldata[k]
        savefile.create_dataset(dgroup + "/" + k, data=data, compression='gzip')

    savefile.close()


# Written by Dr. Farbin
def downsample(y,factor,Nx,Ny,Nz,Nw,sumabs=False):
    if factor==0:
        return np.reshape(y,[Nx,Ny,Nz,Nw]),Nw
    # Remove entries at the end so Down Sampling works
    NwNew=Nw-Nw%factor
    features1=np.reshape(y,[Nx,Ny,Nz,Nw])[:,:,:,0:NwNew]
    # DownSample
    if sumabs:
       features_Down=abs(features1.reshape([Nz*NwNew/factor,factor])).sum(axis=3).reshape([Nx,Ny,Nz,NwNew/factor])
    else:
        features_Down=features1.reshape([Nx,Ny,Nz*NwNew/factor,factor]).sum(axis=3).reshape([Nx,Ny,Nz,NwNew/factor])
    return features_Down, NwNew

#Written by Dr. Farbin
def shuffle_in_unison_inplace(a, b, c=False):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    if type(c) != bool:
        return a[p], b[p], c[p]
    return a[p], b[p]
