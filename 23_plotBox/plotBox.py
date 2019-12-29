import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd
import os

if __name__ == "__main__":
    # 1. load the data
    data_name = 'for_plot.txt'
    data_folder = '/home/beyoung/Desktop/mac-ubuntu-share/2_sensor_alignment/5_sensing_sanChiImu_calibr/extention1_191204+05+09+12_Sensing_JAX92701_close'
    data_label = data_folder[data_folder.rfind('/') + 1:]
    data_path = os.path.join(data_folder, data_name)

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

    # 2. convert list to matrix
    temp_mat = np.array(result_list)
    result_mat = temp_mat.astype(np.float)

    # 3. statistics analysis
    # 3.1 define a column name map
    switch = {
        '0' : 'rotation_x',
        '1' : 'rotation_y',
        '2' : 'rotation_z',
        '3' : 'translation_x',
        '4' : 'translation_y',
        '5' : 'translation_z'
    }

    # 3.2 plot
    for n in range(result_mat.shape[1]):
        column_name = switch.get(str(n))
        column_data = result_mat[:, n]
        # print(pd.DataFrame(column_data).describe())
        plot_box = pd.DataFrame(column_data)
        plot_box.plot.box(title=column_name)
        plt.grid(linestyle="--", alpha=0.3)
        if column_name.find('rotation') != -1:
            plt.ylabel('deg')
        elif column_name.find('translation') != -1:
            plt.ylabel('mm')
        # plt.show()
        # print(data_folder + '191125_original_box_' + column_name + '.jpg')
        save_path = os.path.join(data_folder, column_name + '_box_' + data_label + '.jpg')
        plt.savefig(save_path)
