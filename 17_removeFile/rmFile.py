import os
import shutil

if __name__ == "__main__":
    dataPath = "/home/beyoung/Desktop/mac-ubuntu-share/work/0_Mine/testRm"
    for root, dirs, files, in os.walk(dataPath):
        # remove the directories
        for dirname in dirs:
            if dirname.find("build-") != -1:
                folderPath = os.path.join(root, dirname)
                shutil.rmtree(folderPath)
        # remove the files
        for filename in files:
            if filename.find("CMakeLists.txt.user") != -1:
                filePath = os.path.join(root, filename)
                os.remove(filePath)
