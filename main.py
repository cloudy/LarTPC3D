import LArTPCDNN
import h5py

data = h5py.File("../../data/apr_9/2d/muon_48.2d.h5")
print(data["features"].shape)
