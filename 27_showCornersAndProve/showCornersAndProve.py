import os
import cv2
import numpy as np
import matplotlib.pyplot as mplt

if __name__ == "__main__":
    img_path = "/home/beyoung/Desktop/mac-ubuntu-share/2_sensor_alignment/10_Corner3D_CameraPoseReconstructor/1_data/2_20200312_binyang/Position1/dataSet_5/camNormal1"
    suffix = '.png'
    rows = 4
    cols = 5
    board_size = (cols, rows)
    for root, dirs, files in os.walk(img_path):
        for file in files:
            if (file.find(suffix) != -1) and (file.find('result') < 0):
                # 1. read image
                img = cv2.imread(os.path.join(img_path, file), cv2.IMREAD_UNCHANGED)
                cv2.namedWindow('original image: ' + file, cv2.WINDOW_AUTOSIZE)
                cv2.imshow('original image: ' + file, img)
                # 2. find chessboard and show
                flags = cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE + cv2.CALIB_CB_FAST_CHECK
                ret, obs = cv2.findChessboardCorners(img, board_size)
                cv2.drawChessboardCorners(img, board_size, obs, ret)
                cv2.imshow('found corners', img)
                # 3. plot the corners
                if ret > 0:
                    point_size = len(obs)
                    corners = np.zeros((point_size, 2))
                    for i in range(0, point_size):
                        # print('obs[i]: ' + str(i) + str(obs[i]))
                        temp1 = obs[i]
                        # print('temp1[i]: ' + str(i) + str(temp1))
                        temp2 = temp1[0]
                        # print('temp2[i]: ' + str(i) + str(temp2))
                        corners[i, 0] = temp2[0]
                        corners[i, 1] = temp2[1]
                    fig = mplt.figure()
                    # figure的百分比,从figure 10%的位置开始绘制, 宽高是figure的80%
                    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
                    # 获得绘制的句柄
                    ax = fig.add_axes([left, bottom, width, height])
                    ax.plot(corners[:, 0], corners[:, 1], 'ro-')
                    ax.set_xlabel('x')
                    ax.set_ylabel('y')
                    ax.grid()
                    ax.invert_yaxis()
                    ax.set_title("plot points")
                    mplt.show()
                else:
                    print('original image: ' + file + 'has no corners found')
                #
                cv2.waitKey(50)
                cv2.destroyAllWindows()

