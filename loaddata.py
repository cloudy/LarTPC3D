import h5py




# Written by Dr. Farbin
def DownSample(y,factor,Nx,Ny,Nz,Nw,sumabs=False):
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
