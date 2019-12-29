import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd
import os


def load_data(data_path):
    # 1. load the data
    result_list = []
    file = open(data_path)
    line_number = 0
    for line in file:
        if line == '\n':
            continue
        line = line.strip('\n')
        line = re.split('[(), ]', line)
        line_data = [val for val in line if (val != '[' + str(line_number) + ']') & (val != 'R_BC') & (val != '=') & (val != '') & (val != 'deg') & (val != 'pBC') & (val != 'mm')]
        result_list.append(line_data)
        line_number += 1
    # 2. convert the data from list to matrix
    temp_mat = np.array(result_list)
    result_mat = temp_mat.astype(np.float)
    # 3. return data
    return result_mat


switch = {
    '0': 'rotation_x',
    '1': 'rotation_y',
    '2': 'rotation_z',
    '3': 'translation_x',
    '4': 'translation_y',
    '5': 'translation_z'
}


def plot_comparison(column_name, data_name1, data1, data_name2, data2):
    global data_path
    data = {
        data_name1: data1,
        data_name2: data2
    }
    plot_box = pd.DataFrame(data)
    plot_box.plot.box(title=column_name)
    plt.grid(linestyle="--", alpha=0.3)
    if column_name.find('rotation') != -1:
        plt.ylabel('deg')
    elif column_name.find('translation') != -1:
        plt.ylabel('mm')
    # plt.show()
    # print(data_path + '/comparison/box_comparison' + column_name + '.jpg')
    plt.savefig(data_path + '/box_comparison_' + column_name + '.jpg')


if __name__ == "__main__":
    data_path = "/home/beyoung/Desktop/mac-ubuntu-share/2_sensor_alignment/5_sensing_sanChiImu_calibr/8_20191204VS20191205/comparison"
    data_name1 = '20191204_for_plot.txt'
    data_name2 = '20191205_for_plot.txt'
    # 1. data path
    data1 = load_data(os.path.join(data_path, data_name1))
    data2 = load_data(os.path.join(data_path, data_name2))
    # 2. begin process
    for n in range(data1.shape[1]):
        column_name = switch.get(str(n))
        plot_comparison(column_name, data_name1, data1[:, n], data_name2, data2[:, n])

