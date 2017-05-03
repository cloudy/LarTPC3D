import LArTPCDNN
import ProcessData as pd
import glob
import os

def preprocess(datapath, outputpath, dsfactor = 16):
    filelist2d = glob.glob(datapath + "2d/*")

    for filename in filelist2d:
         fn3d = datapath + "3d/" + os.path.basename(filename).split('.2d.h5')[0] + ".3d.h5"
         data, dataf = pd.loaddata(filename, key="features")         
         data3d = pd.loaddata(fn3d, is3D= True)
         dsdata, samples = pd.downsample(data, dsfactor, *data.shape)
         pd.savedata("2d", dataf, dsdata, "features", outputpath, os.path.basename(filename))


def main():
    # PROCESS DATA 
    inpath = "/data/datasets/LarTPC/apr_9/"
    outpath = "/data/datasets/LarTPC/output/"
    preprocess(inpath, outpath)


    
if __name__ == "__main__":
    main()