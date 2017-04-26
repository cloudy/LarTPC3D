import LArTPCDNN
import ProcessData as pd
import glob
import os

def preprocess(datapath, outputpath, dsfactor = 2):
    filelist = glob.glob(datapath)

    for filename in filelist:
         print "loading: ", filename
         data = pd.loaddata(filename, key="features")
         dsdata, samples = pd.downsample(data, dsfactor, *data.shape)
         pd.savedata(dsdata, outputpath, os.path.basename(filename))


def main():
    # PROCESS DATA 
    path = "/data/datasets/LarTPC/apr_9/2d/*"
    preprocess(path, "/data/datasets/LarTPC/output/", dsfactor = 2)


    
if __name__ == "__main__":
    main()