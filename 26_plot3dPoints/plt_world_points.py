import matplotlib.pyplot as mplt
from mpl_toolkits.mplot3d import Axes3D
import json
import argparse
import numpy as np
import math
import os

def findAdjacentCorners(rows, cols, adjacent_points, len):
    endPos = rows * cols -1
    for pos in range(0, len):
        if ((pos + 1) % cols == 0) and (pos != endPos):
            temp = np.zeros((1, 1))
            temp[0, 0] = pos + cols
        elif ((cols * (rows - 1) - 1) < pos) and (pos < endPos):
            temp = np.zeros((1,1))
            temp[0, 0] = pos + 1
        elif pos == endPos:
            temp = np.zeros((1, 1))
            temp[0, 0] = pos
        else:
            temp = np.zeros((2, 1))
            temp[0, 0] = pos + 1
            temp[1, 0] = pos + cols
        adjacent_points[pos] = temp


def calAdjacentCornersDis(adjacent_points, points_arr, block_size):
    for key in adjacent_points:
        print("-----------------------------------------------------")
        print("current point: " + str(key))
        current_point_arr = points_arr[key, :]
        adjacent_points_index = adjacent_points[key]
        for i in range(len(adjacent_points_index)):
            if adjacent_points_index[i] != key:
                diff_arr = current_point_arr - points_arr[int(adjacent_points_index[i])]
                dist = math.sqrt(diff_arr[0]**2 + diff_arr[1]**2 + diff_arr[2]**2)
                epsilon = 0.5
                if dist - block_size > 0.5:
                    print("wrong distance at adjacent points: " + str(adjacent_points_index[i]) + ", distance: " + str(dist))
                else:
                    print("adjacent points: " + str(adjacent_points_index[i]) + ", distance: " + str(dist))
            else:
                print("The adjacent points of the last point have been considered")


def show(points_arr, result_path):
    fig = mplt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(points_arr[:, 0], points_arr[:, 1], points_arr[:, 2], 'ro-')
    ax.set_xlabel('x/m')
    ax.set_ylabel('y/m')
    ax.set_zlabel('z/m')
    ax.set_title("3d corner points")
    if if_save_fig:
        seg_pos = result_path.rfind("/")
        suffix_pos = result_path.rfind(".")
        save_folder = result_path[0 : seg_pos]
        save_name = result_path[seg_pos + 1 : suffix_pos]
        save_path = os.path.join(save_folder, save_name + ".jpg")
        mplt.savefig(save_path)
    mplt.show()

if __name__ == "__main__":
    if_test = False
    if_show = True
    if_save_fig = False
    if not if_test:
        # 1. parse the input from command line
        # default configs path
        default_configs_path = "../../configs/config.json"
        configs_path = default_configs_path
        # parse from command line
        parser = argparse.ArgumentParser(description='Plot 3D Corner Points And Distance Between Adjacent Corner Points')
        parser.add_argument('--result_path', type=str, required=False, help='Path of result file(timestamp_result.json)')
        parser.add_argument('--configs_path', type=str, required=False, help='Path of configs.json ')
        parser.add_argument('--save_image', type=bool, required=False, help='if save the plotted image')
        args = parser.parse_args()
        if args.result_path == None:
            print('Please input --result_path')
            exit(1)
        else:
            result_path = args.result_path
            print('--result_path: ' + result_path)
        if args.configs_path == None:
            print('No --configs_path has been input, the default will be used: ' + configs_path)
        else:
            configs_path = args.configs_path
            print('--configs_path: ' + configs_path)
        if args.save_image == None:
            print('Plotted image will not to be saved because --save_image is not input')
        else:
            if_save_fig = True
    else:
        print("Test")
        configs_path = "/home/beyoung/Desktop/mac-ubuntu-share/work/8_CameraPoseReconstructor/3_CornerCloudsCamPoseReconstructor/CornerCloudsCamPoseReconstructor/configs/config.json"
        result_path = "/home/beyoung/Desktop/mac-ubuntu-share/2_sensor_alignment/10_Corner3D_CameraPoseReconstructor/1_data/3_20200409/camNormal1/3dCorners_CamPose_Reconstruct_results/m_1587092967_result.json"

    # 2. load parameters
    # 2.1 load chessboard params from configs.json
    with open(configs_path) as configs_file:
        configs = json.load(configs_file)
    chessboard_params_path = configs['ChessboardParamsPath']
    with open(chessboard_params_path) as chessboard_params_file:
        chessboard_params = json.load(chessboard_params_file)
    chessboard_rows = chessboard_params['Rows']
    chessboard_cols = chessboard_params['Cols']
    chessboard_block_size = chessboard_params['BlockSize']
    # print("Rows = " + str(chessboard_rows) + ", Cols = " + str(chessboard_cols) + ", BlockSize = " + str(chessboard_block_size))
    # 2.2 load results: 3D corner points
    # 2.2.1 load points
    result = json.load(open(result_path))
    points = result['3D corners']
    # 2.2.2 convert data into arrays
    points_size = len(points)
    points_arr = np.zeros((points_size, 3))
    index = 0
    for value in points.values():
        points_arr[index, 0] = value[0]
        points_arr[index, 1] = value[1]
        points_arr[index, 2] = value[2]
        index = index + 1

    # 3. Check distance between djacent corner points
    adjacent_points = {}
    # 3.1 find adjacent corner points
    findAdjacentCorners(chessboard_rows, chessboard_cols, adjacent_points, points_size)
    # 3.2 calculate the distance
    calAdjacentCornersDis(adjacent_points, points_arr, chessboard_block_size)

    # 4. plot
    if if_show:
        show(points_arr, result_path)
