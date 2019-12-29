import csv
import os
import xlsxwriter

def get_folder_name(data_path, folders_name):
    for root, dirs, files in os.walk(data_path):
        for dirname in dirs:
            if dirname.find("GMT") != -1:
                folders_name.append(dirname)

def createCsv(target_path, folders_name):
    workbook = xlsxwriter.Workbook(target_path+"/data_performance.xlsx")
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for data_name in folders_name:
        worksheet.write(row, col, data_name)
        row += 1
    workbook.close()

if __name__ == "__main__":
    data_path = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/forSigma/data"
    target_path = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/forSigma"
    folders_name = []
    get_folder_name(data_path, folders_name)
    createCsv(target_path, folders_name)
    print("hello")
