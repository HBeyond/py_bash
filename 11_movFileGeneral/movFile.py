import os
import os.path
import shutil

def movFile(dataPath, targetPath, fileName):
    for root, dirs, files in os.walk(dataPath):
        for dir in dirs:
            if dir.find("GMT") != -1:
                for root2, dirs2, files2 in os.walk(os.path.join(root, dir)):
                    for file2 in files2:
                        if file2.find(fileName) != -1:
                            for root_tar, dirs_tar, files_tar in os.walk(targetPath):
                                for dir_tar in dirs_tar:
                                    if dir_tar == dir:
                                        oldPath = os.path.join(root, dir, file2)
                                        newPath = os.path.join(root_tar, dir_tar, file2)
                                        shutil.copy(oldPath, newPath)
                                        print("b")


if __name__ == "__main__":
    dataPath = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/forSigma/dataOri"
    targetPath = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/Performance/batch/1_0_original_data"
    fileName = "OsmOriSegData.txt"
    movFile(dataPath, targetPath, fileName)
    print("a")