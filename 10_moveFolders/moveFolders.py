import os
import shutil

if __name__ == "__main__":
    data_path = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/forSigma/data"
    target_path = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/forSigma/CityData"
    for root, dirs, files in os.walk(data_path):
        for dirname in dirs:
            if dirname.find("City") != -1:
                shutil.copytree(root+"/"+dirname, target_path+"/"+dirname)  # copy
                shutil.rmtree(root+"/"+dirname)                             # delete the original
                # the two sentences above can be replaced by shutil.move()
                print("1")
