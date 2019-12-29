import os

def getOsmData(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.find("OsmOriSegData.txt") != -1:
                data_path = root + "/OsmOriSegData.txt"
                target_path = root + "/osmData.txt"
                file = open(data_path)
                allData = []
                oneLine = []
                for line in file:
                    line = line[11:-2]
                    for pos in line.split(","):
                        oneLine.append(pos)
                allData.append(oneLine)
                file.close()

                newFile = open(target_path, "a+")
                newFile.write("longitude latitude\n")
                for line in allData:
                    for position in line:
                        newFile.write(position + "\n")
                newFile.close()


if __name__ == "__main__":
    root_path = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/Performance/batch/original/JPN/merge"
    getOsmData(root_path)
