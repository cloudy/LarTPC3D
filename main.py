import LArTPCDNN
import ProcessData



def main():
    data = h5py.File("/data/datasets/LarTPC/apr_9/2d/muon_48.2d.h5")
    print(data["features"].shape)



    
if __name__ == "__main__":
    main()