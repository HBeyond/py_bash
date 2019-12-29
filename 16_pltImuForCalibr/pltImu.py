import numpy as np
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    data_folder = "/home/beyoung/Desktop/mac-ubuntu-share/2_sensor alignment/5_sensing_sanChiImu_calibr/20191017_SensingJaX52202/"
    data_name = []
    imu_data = []
    imu_data_numbers = 0
    # 1. find the data in .csv
    for root, dirs, files in os.walk(data_folder):
        # if dirs:
        #     dir =
        for filename in files:
            if filename.endswith(".csv"):
                data_name.append(filename)
                imu_data_numbers += 1

    # 2. load the data
    for i in range(imu_data_numbers):
        # 2.1 load to list
        one_data_list = []
        csv_file = open(os.path.join(data_folder, data_name[i]))
        for line in csv_file:
            line = line.strip('\n')
            one_line = []
            for pos in line.split(','):
                temp = float(pos)
                if temp > 9:
                    temp -= 9.8
                one_line.append(temp)
            one_data_list.append(one_line)
        csv_file.close()
        # 2.2 convert the list to matrix
        one_data_matrix = np.array(one_data_list)
        one_data_matrix.astype(np.int)
        # 3. plot
        fig = plt.figure('Imu Data ' + str(i))
        plt.subplot(2, 1, 1)
        plt.plot(one_data_matrix[:, 0], one_data_matrix[:, 1], 'r')
        plt.plot(one_data_matrix[:, 0], one_data_matrix[:, 2], 'g')
        plt.plot(one_data_matrix[:, 0], one_data_matrix[:, 3], 'b')
        plt.legend(['x', 'y', 'z'])
        plt.xlabel('serial number')
        plt.ylabel('Rotation')
        plt.title('Rotation')
        plt.grid()
        plt.subplot(2, 1, 2)
        plt.plot(one_data_matrix[:, 0], one_data_matrix[:, 4], 'r')
        plt.plot(one_data_matrix[:, 0], one_data_matrix[:, 5], 'g')
        plt.plot(one_data_matrix[:, 0], one_data_matrix[:, 6], 'b')
        plt.xlabel('serial number')
        plt.ylabel('Acceleration')
        plt.title('Acceleration')
        plt.legend(['x', 'y', 'z'])
        plt.grid()
        plt.savefig(data_folder + 'Imu_Data_' + str(i) + '.eps')

    plt.show()



