dataPath = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/20190222/jpn_tunnel2/GpsLostEnoughData/2017-09-01_T_04-33-20.262_GMT/result_0225_imuGpsOsmOpt_0001/match.txt"


import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    f = open(dataPath)
    line = f.readline()
    data_list = []
    while line:
        num = list(map(float,line.split(',')))
        data_list.append(num)
        line = f.readline()
    f.close()
    data_array = np.array(data_list)
    print(data_array)

    plt.plot(data_array[:,0],data_array[:,1])
    plt.show()