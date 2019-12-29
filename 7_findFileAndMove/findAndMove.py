import os       # adverse the root path
import shutil   # copy file to another path

def detect_copy(data_path, target_path, findImu):
    for root, dirs, files in os.walk(data_path):
        for dirname in dirs:
            print("dir:%s\n" % dirname)
        for filename in files:                            # if list files is not empty
            if filename.find("GMT.gps") != -1:            # if list find the file whose name contains string "GMT.gps". Return -1 means failure, but 1 not means right.
                print("filename:%s\n" % filename)         # first check the GMT.gps file
                if findImu == -1:
                    # only move gps to folder for getting csv
                    shutil.copy(root + "/" + filename, target_path + "/" + filename)           # for get csv folder
                # move both gps and imu to merged folder
                if findImu != -1:
                    folder_name = filename[:-4]               # if GMT.gps file exists, then get the name
                    os.makedirs(target_path+"/"+folder_name)  # and make a dir
                    shutil.copy(root+"/"+filename, target_path+"/"+folder_name+"/"+filename)    # for merged folder, copy the file from original path to target path
        if findImu != -1:
            for filename in files:                            # then check the GMT.imu file. Actually this can be carried out with GMT.gps file check at the same time
                if filename.find("GMT.imu") != -1:            # but for extension, they are desperate
                    print("filename:%s\n" % filename)
                    folder_name_imu = filename[:-4]
                    isExitst = os.path.exists(target_path+"/"+folder_name_imu)    # check this folder exists, that is check if there are the same name GMT.gps file
                    if isExitst:
                        shutil.copy(root+"/"+filename, target_path+"/"+folder_name_imu+"/"+filename)


def removeOneFileFolder(target_path):                      # because GMT.gps and GMT.imu are desperate, so there are some folders may only have one GMT.gps file
    for root, dirs, files in os.walk(target_path):        # they have to be removed
        if (files.__len__() == 1):
            if (files[0].find("GMT.gps") != -1):
                os.remove(root+"/"+files[0])          # first remove the file
                os.rmdir(root)                        # them remove the empty dir

if __name__ == "__main__":
    data_path = "/Users/user/Desktop/mac-ubuntu-share/ReferenceGPSCollection/NewData2/zip"
    target_path = "/Users/user/Desktop/mac-ubuntu-share/ReferenceGPSCollection/NewData2/merge"
    findImu = 1
    detect_copy(data_path, target_path, findImu)
    if findImu != -1:
        removeOneFileFolder(target_path)