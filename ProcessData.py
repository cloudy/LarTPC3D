import h5py
import os


def LoadData(Path, SpecificFile = None):
    if (SpecificFile != None):
        return 


# Written by Dr. Farbin
def OrganizeFiles(Files):
    FileCount= {}  # Store the count here
    FileLists= {}  # Organize the files by particle type here.

    for aFile in Files:
        # Lets strip the path (everything before the "/"s) and get the filename:
        FileName=os.path.basename(aFile)
    
        # Now use everything before the first "_" as the particle name
        ParticleName=FileName.split('_')[0]
    
        if ParticleName in FileCount.keys():
            FileCount[ParticleName]+=1
            FileLists[ParticleName].append(aFile)
        else:
            FileCount[ParticleName]=1
            FileLists[ParticleName]= [aFile]
    
    print "Number of types of particles:", len(FileCount.keys())
    print "----------------------------------------------------------"
    print "Number of files for each particle type:", FileCount
    print "----------------------------------------------------------"
    print "First file of each type:"
    for aFile in FileLists:
        print aFile,":",FileLists[aFile][0]
        
    return FileLists,FileCount


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
