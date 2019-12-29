import os
import os.path
import shutil


def backUp(dataPath, resetFlag):
    if resetFlag == -1:
        for root, dirs, files in os.walk(dataPath):
            for file in files:
                suffix = file[-3:]
                if suffix == "gps":
                    os.rename(root+"/"+file, root+"/"+file+"ori")
                    shutil.copy(root+"/"+file+"ori", root+"/"+file)


def eraseGps(dataPath, resetFlag):
    if resetFlag == -1:
        for root, dirs, files in os.walk(dataPath):
            for file in files:
                suffix = file[-3:]
                if suffix == "gps":
                    gpsFile = open(root+"/"+file, 'r')
                    datas = gpsFile.readlines()
                    gpsFile.close()
                    delMark = [int(datas.__len__() / 3), int(datas.__len__() / 3 * 2)]

                    offsetFactor = [20, 40]  # erase 40 points at delMark[0], 80 points at delMark[1]
                    markBorder = [delMark[0] - offsetFactor[0], delMark[0] + offsetFactor[0], delMark[1] - offsetFactor[0] * 2 - offsetFactor[1], delMark[1] - offsetFactor[0] * 2 + offsetFactor[1]]

                    del datas[markBorder[0]: markBorder[1]]    # erase at delMark[0]
                    #del datas[markBorder[2]: markBorder[3]]

                    gpsFileNew = open(root+"/"+file, 'w')
                    gpsFileNew.writelines(datas)
                    gpsFileNew.close()
                    print("erase successfully")


def resetGpsState(dataPath, resetFlag):
    if resetFlag == 1:
        for root, dirs, files in os.walk(dataPath):
            for file in files:
                suffix = file[-3:]
                if suffix == "gps":
                    os.remove(root+"/"+file)

                    for root2, dirs2, files2 in os.walk(root):
                        for file2 in files2:
                            suffix = file2[-3:]
                            if suffix == "ori":
                                filename = file2[:-3]
                                os.rename(root+"/"+file2, root+"/"+filename)

if __name__ == "__main__":
    dataPath = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/Performance/batch/original/JPN/forCSV"
    resetFlag = -1
    resetGpsState(dataPath, resetFlag)
    backUp(dataPath, resetFlag)
    eraseGps(dataPath, resetFlag)