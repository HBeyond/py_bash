import numpy as np
import matplotlib.pyplot as plt
import re
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

    # 2. convert list to matrxi
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

    # 3.2 calculate the mean, var and std of each column
    mean_val = np.mean(result_mat, axis=0)
    print(mean_val)
    var_val = np.var(result_mat, axis=0, ddof=1)
    print(var_val)
    std_val = np.std(result_mat, axis=0, ddof=1)
    print(std_val)


    # 3.3 plot
    for n in range(result_mat.shape[1]):
        column_name = switch.get(str(n))
        column_data = result_mat[:, n]
        # 3.3 plot the histgram
        plt.figure(n)
        plt.hist(column_data, bins=result_mat.shape[1], alpha=0.5, histtype='bar', rwidth=0.5, color='steelblue', edgecolor='black')
        plt.vlines(mean_val[n], 0, 10)
        plt.text(mean_val[n], 10, 'mean = ' + str(mean_val[n]))
        plt.title(column_name)
        plt.xlabel(column_name)
        plt.ylabel('numbers')
        plt.grid()
        save_path = os.path.join(data_folder, column_name + '_histgram_' + data_label + '.jpg')
        plt.savefig(save_path)

    # plt.show()