import cv2
import os
import shutil
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Show and pick images')
    parser.add_argument('--imgFolder', type=str, required=False, help='original image folder')
    parser.add_argument('--targetFolder', type=str, required=False, help='target image folder')
    args = parser.parse_args()
    if args.imgFolder == None:
        print('Please input --imgFolder')
        exit(1)
    else:
        imgFolder = args.imgFolder
        print('--imgFolder: ' + imgFolder)
    if args.targetFolder == None:
        print('Please input --targetFolder')
        exit(1)
    else:
        targetFolder = args.targetFolder
        print('--targetFolder: ' + targetFolder)

    print('Press Enter to pick, Esc to exit or others to skip')

    for root, dirs, files in os.walk(imgFolder):
        for filename in files:
            if filename.find('.png') != -1:
                imgPath = os.path.join(root, filename)
                img = cv2.imread(imgPath)
                patternsize = (4, 5)
                ret, obs = cv2.findChessboardCorners(img, patternsize)
                cv2.drawChessboardCorners(img, patternsize, obs, ret)
                cv2.imshow('img', img)
                key = cv2.waitKey(0)
                if (key == 13):
                    targetImgPath = os.path.join(targetFolder, filename)
                    shutil.copy(imgPath, targetImgPath)
                elif (key == 27):
                    exit()
                else:
                    continue
        print('All the images have been traversed')


