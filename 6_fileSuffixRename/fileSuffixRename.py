import os
import os.path

def fileRename(dataPath, suffix, newSuffix):
    suffixLength = suffix.__len__()
    for root, dirs, files in os.walk(dataPath):
        for filename in files:
            if filename.find(suffix) != -1:
                nameNoSuffix = filename[:(-suffixLength)]
                oldName = nameNoSuffix + suffix
                newName = nameNoSuffix + newSuffix
                os.renames(os.path.join(root, oldName), os.path.join(root, newName))
                print("b")


if __name__ == "__main__":
    dataPath = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/forSigma/dataOri"
    suffix = ".gpsori"
    newSuffix = ".gps"
    fileRename(dataPath, suffix, newSuffix)
    print("a")