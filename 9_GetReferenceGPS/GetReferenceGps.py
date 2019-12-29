import os
import shutil

if __name__ == "__main__":
    dataPath = "/Users/user/Desktop/mac-ubuntu-share/ReferenceGPSCollection/NewData3/oriData"
    targetPath = "/Users/user/Desktop/mac-ubuntu-share/ReferenceGPSCollection/NewData3/DgpsData"

    for root, dirs, files in os.walk(dataPath):
        for dirname in dirs:
            if dirname.find("UTC") != -1:
                dataFolder = os.path.join(root, dirname)
                for root2, dirs2, files2 in os.walk(dataFolder):
                    hasRawGps = False
                    hasGps = False
                    hasImu = False
                    isDgps = False
                    gpsPath = "null"
                    gpsFileName = "null"
                    rawGpsPath = "null"
                    rawGpsFileName = "null"
                    imuPath = "null"
                    imuFileName = "null"
                    # iterate the files dataFolder
                    for filename2 in files2:
                        if filename2.find(".DGPS.gps") != -1:
                            hasGps = True
                            gpsPath = os.path.join(root2, filename2)
                            gpsFileName = filename2
                        elif filename2.find(".DGPS.rawgps") != -1:
                            hasRawGps = True
                            rawGpsPath = os.path.join(root2, filename2)
                            rawGpsFileName = filename2
                        elif filename2.find(".sbg.imu") != -1:
                            hasImu = True
                            imuPath = os.path.join(root2, filename2)
                            imuFileName = filename2
                    # check if has two files and if it is DGPS
                    if hasRawGps and hasGps and hasImu:
                        file = open(rawGpsPath)
                        for line in file:
                            lineData = line.split(",")
                            print(lineData[0])
                            if lineData[0] == "$GPGGA":
                                print(lineData[0])
                                if lineData[6] == "2":
                                    print(lineData[6])
                                    # copy the .gps, .rawgps and imu to another path
                                    targetPathFolder = os.path.join(targetPath, dirname)
                                    if os.path.exists(targetPathFolder):
                                        break
                                    else:
                                        os.makedirs(targetPathFolder)
                                        targetGpsPath = os.path.join(targetPathFolder, gpsFileName)
                                        targetRawGpsPath = os.path.join(targetPathFolder, rawGpsFileName)
                                        targetImuPath = os.path.join(targetPathFolder, imuFileName)
                                        shutil.copy(str(gpsPath), str(targetGpsPath))
                                        # shutil.copy(str(rawGpsPath), str(targetRawGpsPath))
                                        shutil.copy(str(imuPath), str(targetImuPath))
                                elif lineData[6] != "2":
                                    print(lineData[6])
                                    print(dirname + " does not contain a DGPS file")
                                    break


