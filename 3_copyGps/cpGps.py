import os
import shutil

if __name__=="__main__":
    data_path = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/forSigma/data"

    for root, dirs, files in os.walk(data_path):
        for filename in files:
            if filename.find(".gps") != -1:
                shutil.copy(root+"/"+filename, root+"/"+filename+"ori")