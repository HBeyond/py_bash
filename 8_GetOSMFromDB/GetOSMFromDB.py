import os
import csv  # read osm_id from csv
import psycopg2

def getOsmId(file_path):
    print("get osmid from csv")
    with open(file_path, 'rt') as csvfile:          # open the csv file
        reader = csv.DictReader(csvfile)
        column = [row['OsmId'] for row in reader]   # read the row named OsmId
        uniq_column = list(set(column))             # get rid of the repeatable elements
        uniq_column.sort(key = column.index)        # sort the list due to the index of original list after the step above
        return uniq_column

def dbOperation(uniq_osmId):
    print("db operation begin")
    # connect to db
    conn = psycopg2.connect(database=db_county, user="ygomi_gis", password="r0addb&123", host="127.0.0.1", port="5432")
    # consult
    currentReslt = []
    cur = conn.cursor()
    for index in uniq_osmId:
        cur.execute("select osm_id, ST_AsText(ST_Transform(way,4326)) from planet_osm_line where osm_id =" + index)
        temp = cur.fetchone()
        currentReslt.append(temp[1])
    # disconnect
    cur.close()
    conn.close()
    # return list
    return currentReslt

def save(resultList, dataName, savePath):
    print("save begin")
    dataPath = savePath + "/" + dataName + "/" + "OsmOriSegData.txt"
    # fileExist = os._exists(dataPath)
    # if
    fileObject = open(dataPath, 'w')
    for line in resultList:
        fileObject.write(line)
        fileObject.write('\n')
    fileObject.close()

def process(csv_path, savePath):
    print("process begin")
    for root, dirs, files in os.walk(csv_path):     # path iterator begins
        for filename in files:                      # files in path iterator begins
            if filename.find(".csv") != -1:
                uniq_osmId = getOsmId(root+"/"+filename)    # get the nonredundant OsmId
                # database operation
                resultList = dbOperation(uniq_osmId)
                dataName = filename[:-4]
                save(resultList, dataName, savePath)


if __name__ == "__main__":
    csvPath = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/Performance/batch/original/JPN/forCSV"
    savePath = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/Performance/batch/original/JPN/merge"
    db_county = "JPN"
    process(csvPath, savePath)
