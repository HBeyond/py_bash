import os
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data_path = "/home/beyoung/Desktop/mac-ubuntu-share/2_sensor_alignment/5_sensing_sanChiImu_calibr/10_20191209_SensingJaX92701_behind_results/rs_calibration/SensingJAX92701"
    write_file = open(os.path.join(data_path, 'statistics.txt'), 'w')
    # 1. get line_delays, intrinsics and distortion
    line_delays_intrinsics_distortion = []
    for root, dirs, files in os.walk(data_path):
        for filename in files:
            if filename.find("rs_calibration.txt") != -1:
                file = open(os.path.join(root, filename))
                cout = False
                for line in file:
                    line_str = str(line)
                    if cout:
                        # 1.2 write into a txt
                        # print(line)
                        line_delays_intrinsics_distortion.append(line)
                        write_file.write(line + '\n')
                    if line.find("[3] Adaptive Knot Placement") != -1:
                        cout = True
                        data_name = root[-6:]
                        # 1.1 write into a txt
                        line_delays_intrinsics_distortion.append('\n')
                        line_delays_intrinsics_distortion.append("=================================\n")
                        line_delays_intrinsics_distortion.append(data_name)
                        write_file.write('\n')
                        write_file.write("=================================\n")
                        write_file.write(data_name + '\n')

    # 2. get the line delays and plot the histgram
    line_delays = []
    for n in range(len(line_delays_intrinsics_distortion)):
        if line_delays_intrinsics_distortion[n].find("LineDelay") != -1:
            line_delays_string = line_delays_intrinsics_distortion[n].strip('\n')
            line_delays_data = line_delays_string[line_delays_string.find(':') + 1:]
            line_delays.append(line_delays_data)
    # 3. convert line_delays to matrix
    line_delays_mat = np.array(line_delays)
    line_delays_mat = line_delays_mat.astype(np.float)
    # 4. plot
    for n in range(line_delays_mat.size):
        line_delays_mat[n] *= (10.0**5)
    # 4.1 calculate the mean
    mean = line_delays_mat.mean()
    mean_mat = np.ones(line_delays_mat.size) * mean
    # 4.2 find the max and the min in line_delays_mat
    line_delays_mat_max = line_delays_mat.max()
    line_delays_mat_max_mat = np.ones(line_delays_mat.size) * line_delays_mat_max
    line_delays_mat_min = line_delays_mat.min()
    line_delays_mat_min_mat = np.ones(line_delays_mat.size) * line_delays_mat_min
    extreme_arr = np.array([line_delays_mat_min, line_delays_mat_max])
    extreme_x = np.ones(2) * (line_delays_mat.size - 1)
    # 4.3 create the x bar
    column_x = np.zeros(line_delays_mat.size)
    for n in range(line_delays_mat.size):
        column_x[n] = n + 1
    # 4.4 begin plot
    plt.figure()
    plt.plot(column_x, line_delays_mat, 'ro-')
    plt.plot(column_x, mean_mat, 'b-')
    plt.text(column_x[0], mean + 0.001, 'mean = ' + str(mean) + '$*10^{-5}s$')
    plt.plot(column_x, line_delays_mat_max_mat, 'c--')
    plt.plot(column_x, line_delays_mat_min_mat, 'm--')
    plt.plot(extreme_x, extreme_arr, 'g--')
    plt.text(extreme_x[0] - 20, (line_delays_mat_max + line_delays_mat_min) / 2, 'max - min = ' + str(line_delays_mat_max - line_delays_mat_min) + '$*10^{-5}s$')
    plt.xlabel('data_serial')
    plt.ylabel('line delay time/$10^{-5}$s')
    plt.legend(['line delay', 'mean', 'max', 'min', 'max - min'])
    plt.grid()
    # plt.show()
    plt.savefig(os.path.join(data_path, 'statistics.jpg'))