import os       # adverse the root path
import shutil   # copy file to another path
import numpy as np

def calSigma(data, sigma):
    # prepare the data
    rows = len(data)
    print(rows)
    data_mat = np.zeros((rows, 4))
    dis_ang_err = np.zeros((rows-1, 2))

    for row in range(rows):
        data_mat[row][0] = data[row][1]
        data_mat[row][1] = data[row][2]
        data_mat[row][2] = data[row][4]
        data_mat[row][3] = data[row][5]
    # distance calculation
    for row in range(rows-1):
        # get each vector
        last_opt = np.mat([data_mat[row][0],data_mat[row][1]])
        next_opt = np.mat([data_mat[row+1][0],data_mat[row+1][1]])
        last_osm = np.mat([data_mat[row][2], data_mat[row][3]])
        next_osm = np.mat([data_mat[row + 1][2], data_mat[row + 1][3]])
        # inner error
        opt_error = last_opt - next_opt
        osm_error = last_osm - next_osm
        # distance calculation
        dis_opt = np.sqrt(opt_error*(opt_error.T))
        dis_osm = np.sqrt(osm_error*(osm_error.T))
        print(dis_opt)
        print(dis_osm)
        disErr = dis_osm - dis_opt
        print(disErr)
        # angle calculation
        last_osm_norm = np.sqrt(last_osm*(last_osm.T))
        next_osm_norm = np.sqrt(next_osm*(next_osm.T))
        cos_ang_osm = (last_osm * (next_osm.T)) / (last_osm_norm * next_osm_norm)
        ang_osm = np.arccos(cos_ang_osm)
        last_opt_norm = np.sqrt(last_opt*(last_opt.T))
        next_opt_norm = np.sqrt(next_opt*(next_opt.T))
        cos_ang_opt = (last_opt * (next_opt.T)) / (last_opt_norm * next_opt_norm)
        ang_opt = np.arccos(cos_ang_opt)
        angErr = ang_osm - ang_opt
        print(angErr)
        dis_ang_err[row] = [disErr, angErr]
    # calculate the sigma
    sigma_dis_err = np.std(dis_ang_err[:,0])
    sigma_ang_err = np.std(dis_ang_err[:,1])
    # check the calculation method
    # all_dis_err = dis_ang_err[:,0]
    # all_ang_err = dis_ang_err[:,1]
    # # calculate sigma for dis
    # ave_dis_err = sum(all_dis_err)/(rows-1)
    # sum_dis_err_ave_p2 = 0
    # for row in range(rows-1):
    #     sum_dis_err_ave_p2 += np.power(all_dis_err[row] - ave_dis_err,2)
    # sigma_dis_err = np.sqrt(sum_dis_err_ave_p2/(rows-1))
    # # calculate sigma for ang
    # ave_ang_err = sum(all_ang_err)/(rows-1)
    # sum_ang_err_ave_p2 = 0
    # for row in range(rows-1):
    #     sum_ang_err_ave_p2 += np.power(all_ang_err[row] - ave_ang_err,2)
    # sigma_ang_err = np.sqrt(sum_ang_err_ave_p2/(rows-1))
    sigma.append([sigma_dis_err ,sigma_ang_err])
    print("hello")

def findFile(file_path, sigma):
    for root, dirs, files in os.walk(file_path):
        # for dirname in dirs:
        #     print("dir:%s\n" % dirname)
        for filename in files:
            if filename.find("match.txt") != -1:
                data_path = root + "/" + filename
                f = open(data_path)
                lines = f.readlines()
                data = []
                for line in lines:
                    line_seg = line.split(',')   # divide the datas with ','
                    data.append(line_seg)
                # print(data[0][2])
                calSigma(data, sigma)


if __name__ == "__main__":
    file_path = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/forSigma/data"
    sigma = []
    findFile(file_path, sigma)
    rows = len(sigma)
    sigma_mat = np.zeros((rows,2))
    for row in range(rows):
        sigma_mat[row][0] = sigma[row][0]
        sigma_mat[row][1] = sigma[row][1]
    dis_array = sigma_mat[:,0]
    ang_array = sigma_mat[:,1]
    aveSigma_dis = np.sum(dis_array)/len(dis_array)
    aveSigma_ang = np.sum(ang_array)/len(ang_array)
    print("aveSigma_dis = " + str(aveSigma_dis))
    print("aveSigma_ang = " + str(aveSigma_ang))
    print("hello")
