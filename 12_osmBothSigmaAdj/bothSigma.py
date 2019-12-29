# this code is for the average and variance calculation in the experience where
# the ang sigma changes but dis sigma fixed

import os
import numpy as np
import matplotlib.pyplot as plt

def getData(dataPath, gps_averages, gps_variances, osm_averages, osm_variances, factor):
    for root, dirs, files in os.walk(dataPath):
        for dirname in dirs:
            if dirname.find("GMT") != -1:
                subDataPath = dataPath + "/" +dirname
                for subRoot, subDirs, subFiles in os.walk(subDataPath):
                    for subDirname in subDirs:
                        if subDirname.find(factor) != -1:
                            targetDataPath = subDataPath + "/" + subDirname
                            for tarRoot, tarDir, tarFiles in os.walk(targetDataPath):
                                for tarFilename in tarFiles:
                                    # get the gps indicators
                                    if tarFilename.find("gps_Indicators.txt") != -1:
                                        with open(tarRoot + "/" + tarFilename) as gpsIndicators:
                                            lines = gpsIndicators.readlines()
                                            gps_variances.append(lines.pop().split(","))  # the order of these next two lines must be fixed
                                            gps_averages.append(lines.pop().split(","))
                                    # get the osm indicators
                                    elif tarFilename.find("osm_Indicators.txt") != -1:
                                        with open(tarRoot + "/" + tarFilename) as osmIndicators:
                                            lines = osmIndicators.readlines()
                                            osm_variances.append(lines.pop().split(","))  # the order of these next two lines must be fixed
                                            osm_averages.append(lines.pop().split(","))

def dataProcess(gps_averages, gps_variances, osm_averages, osm_variances,\
                colAve_gps_averages_array, colVar_gps_averages_array, colAve_gps_variances_array, colVar_gps_variances_array, \
                colAve_osm_averages_array, colVar_osm_averages_array, colAve_osm_variances_array, colVar_osm_variances_array):
    # gps indicators
    gps_averages_array = np.array(gps_averages).astype(float)
    gps_variances_array = np.array(gps_variances).astype(float)
    np.mean(gps_averages_array, axis=0, out=colAve_gps_averages_array)
    np.abs(colAve_gps_averages_array, out=colAve_gps_averages_array)
    np.var(gps_averages_array, axis=0, out=colVar_gps_averages_array)
    np.mean(gps_variances_array, axis=0, out=colAve_gps_variances_array)
    np.var(gps_variances_array, axis=0, out=colVar_gps_variances_array)
    # osm indicators
    osm_averages_array = np.array(osm_averages).astype(float)
    osm_variances_array = np.array(osm_variances).astype(float)
    np.mean(osm_averages_array, axis=0, out=colAve_osm_averages_array)
    np.abs(colAve_osm_averages_array, colAve_osm_averages_array)
    np.var(osm_averages_array, axis=0, out=colVar_osm_averages_array)
    np.mean(osm_variances_array, axis=0, out=colAve_osm_variances_array)
    np.var(osm_variances_array, axis=0, out=colVar_osm_variances_array)

def drawBar_gps(gps1_25, gps02_18, gps001_10, gps001_1, gps0018_10, ylabel, title, tables):
    n_groups = 6
    plt.figure()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.9
    plt.bar(index, gps1_25, bar_width, alpha=opacity, color='b', label='$\sigma_{osm-ang}=1, \sigma_{osm-dis}=25$')
    plt.bar(index + bar_width, gps02_18, bar_width, alpha=opacity, color='g', label='$\sigma_{osm-ang}=0.2, \sigma_{osm-dis}=18$')
    plt.bar(index + bar_width*2, gps001_10, bar_width, alpha=opacity, color='y', label='$\sigma_{osm-ang}=0.01, \sigma_{osm-dis}=10$')
    plt.bar(index + bar_width*3, gps001_1, bar_width, alpha=opacity, color='r', label='$\sigma_{osm-ang}=0.01, \sigma_{osm-dis}=1$')
    plt.bar(index + bar_width*4, gps0018_10, bar_width, alpha=opacity, color='c', label='$\sigma_{osm-ang}=0.018, \sigma_{osm-dis}=10$')
    plt.xlabel('gps residuals comparison at each direction')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks()
    plt.xticks(index + bar_width, tables)
    plt.legend()
    plt.savefig(dataPath[:-4] + "/" + ylabel)

def drawBar_osm(osm1_25, osm02_18, osm001_10, osm001_1, osm0018_10, ylabel, title, tables):
    n_groups = 4
    plt.figure()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.9
    plt.bar(index, osm1_25, bar_width, alpha=opacity, color='b', label='$\sigma_{osm-ang}=1, \sigma_{osm-dis}=25$')
    plt.bar(index + bar_width, osm02_18, bar_width, alpha=opacity, color='g', label='$\sigma_{osm-ang}=0.2, \sigma_{osm-dis}=18$')
    plt.bar(index + bar_width*2, osm001_10, bar_width, alpha=opacity, color='y', label='$\sigma_{osm-ang}=0.01, \sigma_{osm-dis}=10$')
    plt.bar(index + bar_width*3, osm001_1, bar_width, alpha=opacity, color='r', label='$\sigma_{osm-ang}=0.01, \sigma_{osm-dis}=1$')
    plt.bar(index + bar_width*4, osm0018_10, bar_width, alpha=opacity, color='c', label='$\sigma_{osm-ang}=0.018, \sigma_{osm-dis}=10$')
    plt.xlabel('osm residuals comparison at relative angle and relative distance')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks()
    plt.xticks(index + bar_width, tables)
    plt.legend()
    plt.savefig(dataPath[:-4] + "/" + ylabel)

if __name__=="__main__":
    dataPath = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/forSigma/data"

    # 1_25
    gps_averages1_25 = []
    gps_variances1_25 = []
    osm_averages1_25 = []
    osm_variances1_25 = []
    getData(dataPath, gps_averages1_25, gps_variances1_25, osm_averages1_25, osm_variances1_25, "0402_Sigma-ori-1-25-dis")
    colAve_gps_averages1_25_array = np.zeros(shape=6)
    colVar_gps_averages1_25_array = np.zeros(shape=6)
    colAve_gps_variances1_25_array = np.zeros(shape=6)
    colVar_gps_variances1_25_array = np.zeros(shape=6)
    colAve_osm_averages1_25_array = np.zeros(shape=4)
    colVar_osm_averages1_25_array = np.zeros(shape=4)
    colAve_osm_variances1_25_array = np.zeros(shape=4)
    colVar_osm_variances1_25_array = np.zeros(shape=4)
    dataProcess(gps_averages1_25, gps_variances1_25, osm_averages1_25, osm_variances1_25,  \
                colAve_gps_averages1_25_array, colVar_gps_averages1_25_array, colAve_gps_variances1_25_array, colVar_gps_variances1_25_array, \
                colAve_osm_averages1_25_array, colVar_osm_averages1_25_array, colAve_osm_variances1_25_array, colVar_osm_variances1_25_array)

    # 02_18
    gps_averages02_18 = []
    gps_variances02_18 = []
    osm_averages02_18 = []
    osm_variances02_18 = []
    getData(dataPath, gps_averages02_18, gps_variances02_18, osm_averages02_18, osm_variances02_18, "0402_Sigma-ori-02-18-dis")
    colAve_gps_averages02_18_array = np.zeros(shape=6)
    colVar_gps_averages02_18_array = np.zeros(shape=6)
    colAve_gps_variances02_18_array = np.zeros(shape=6)
    colVar_gps_variances02_18_array = np.zeros(shape=6)
    colAve_osm_averages02_18_array = np.zeros(shape=4)
    colVar_osm_averages02_18_array = np.zeros(shape=4)
    colAve_osm_variances02_18_array = np.zeros(shape=4)
    colVar_osm_variances02_18_array = np.zeros(shape=4)
    dataProcess(gps_averages02_18, gps_variances02_18, osm_averages02_18, osm_variances02_18,  \
                colAve_gps_averages02_18_array, colVar_gps_averages02_18_array, colAve_gps_variances02_18_array, colVar_gps_variances02_18_array, \
                colAve_osm_averages02_18_array, colVar_osm_averages02_18_array, colAve_osm_variances02_18_array, colVar_osm_variances02_18_array)

    # 001_10
    gps_averages001_10 = []
    gps_variances001_10 = []
    osm_averages001_10 = []
    osm_variances001_10 = []
    getData(dataPath, gps_averages001_10, gps_variances001_10, osm_averages001_10, osm_variances001_10,
            "0402_Sigma-ori-001-10-dis")
    colAve_gps_averages001_10_array = np.zeros(shape=6)
    colVar_gps_averages001_10_array = np.zeros(shape=6)
    colAve_gps_variances001_10_array = np.zeros(shape=6)
    colVar_gps_variances001_10_array = np.zeros(shape=6)
    colAve_osm_averages001_10_array = np.zeros(shape=4)
    colVar_osm_averages001_10_array = np.zeros(shape=4)
    colAve_osm_variances001_10_array = np.zeros(shape=4)
    colVar_osm_variances001_10_array = np.zeros(shape=4)
    dataProcess(gps_averages001_10, gps_variances001_10, osm_averages001_10, osm_variances001_10, \
                colAve_gps_averages001_10_array, colVar_gps_averages001_10_array, colAve_gps_variances001_10_array,
                colVar_gps_variances001_10_array, \
                colAve_osm_averages001_10_array, colVar_osm_averages001_10_array, colAve_osm_variances001_10_array,
                colVar_osm_variances001_10_array)

    # 001_1
    gps_averages001_1 = []
    gps_variances001_1 = []
    osm_averages001_1 = []
    osm_variances001_1 = []
    getData(dataPath, gps_averages001_1, gps_variances001_1, osm_averages001_1, osm_variances001_1,
            "0402_Sigma-ori-001-1-dis")
    colAve_gps_averages001_1_array = np.zeros(shape=6)
    colVar_gps_averages001_1_array = np.zeros(shape=6)
    colAve_gps_variances001_1_array = np.zeros(shape=6)
    colVar_gps_variances001_1_array = np.zeros(shape=6)
    colAve_osm_averages001_1_array = np.zeros(shape=4)
    colVar_osm_averages001_1_array = np.zeros(shape=4)
    colAve_osm_variances001_1_array = np.zeros(shape=4)
    colVar_osm_variances001_1_array = np.zeros(shape=4)
    dataProcess(gps_averages001_1, gps_variances001_1, osm_averages001_1, osm_variances001_1, \
                colAve_gps_averages001_1_array, colVar_gps_averages001_1_array, colAve_gps_variances001_1_array,
                colVar_gps_variances001_1_array, \
                colAve_osm_averages001_1_array, colVar_osm_averages001_1_array, colAve_osm_variances001_1_array,
                colVar_osm_variances001_1_array)

    # 0018_10
    gps_averages0018_10 = []
    gps_variances0018_10 = []
    osm_averages0018_10 = []
    osm_variances0018_10 = []
    getData(dataPath, gps_averages0018_10, gps_variances0018_10, osm_averages0018_10, osm_variances0018_10,
            "0402_Sigma-ori-0018-10-dis")
    colAve_gps_averages0018_10_array = np.zeros(shape=6)
    colVar_gps_averages0018_10_array = np.zeros(shape=6)
    colAve_gps_variances0018_10_array = np.zeros(shape=6)
    colVar_gps_variances0018_10_array = np.zeros(shape=6)
    colAve_osm_averages0018_10_array = np.zeros(shape=4)
    colVar_osm_averages0018_10_array = np.zeros(shape=4)
    colAve_osm_variances0018_10_array = np.zeros(shape=4)
    colVar_osm_variances0018_10_array = np.zeros(shape=4)
    dataProcess(gps_averages0018_10, gps_variances0018_10, osm_averages0018_10, osm_variances0018_10, \
                colAve_gps_averages0018_10_array, colVar_gps_averages0018_10_array, colAve_gps_variances0018_10_array,
                colVar_gps_variances0018_10_array, \
                colAve_osm_averages0018_10_array, colVar_osm_averages0018_10_array, colAve_osm_variances0018_10_array,
                colVar_osm_variances0018_10_array)

    # # 0018_10
    # gps_averages0018_10 = []
    # gps_variances0018_10 = []
    # osm_averages0018_10 = []
    # osm_variances0018_10 = []
    # getData(dataPath, gps_averages0018_10, gps_variances0018_10, osm_averages0018_10, osm_variances0018_10,
    #         "result_0321_testSigma-005-1")
    # colAve_gps_averages0018_10_array = np.zeros(shape=6)
    # colVar_gps_averages0018_10_array = np.zeros(shape=6)
    # colAve_gps_variances0018_10_array = np.zeros(shape=6)
    # colVar_gps_variances0018_10_array = np.zeros(shape=6)
    # colAve_osm_averages0018_10_array = np.zeros(shape=4)
    # colVar_osm_averages0018_10_array = np.zeros(shape=4)
    # colAve_osm_variances0018_10_array = np.zeros(shape=4)
    # colVar_osm_variances0018_10_array = np.zeros(shape=4)
    # dataProcess(gps_averages0018_10, gps_variances0018_10, osm_averages0018_10, osm_variances0018_10, \
    #             colAve_gps_averages0018_10_array, colVar_gps_averages0018_10_array, colAve_gps_variances0018_10_array,
    #             colVar_gps_variances0018_10_array, \
    #             colAve_osm_averages0018_10_array, colVar_osm_averages0018_10_array, colAve_osm_variances0018_10_array,
    #             colVar_osm_variances0018_10_array)

    # draw
    # gps
    tables = ['ER', 'ERO', 'NR', 'NRO', 'UR', 'URO']
    # averages
    ylabel_gps_ave = "gps_residual_averages(meter)"
    title_gps_ave = "gps indicators: residuals averages"
    drawBar_gps(colAve_gps_averages1_25_array, colAve_gps_averages02_18_array, colAve_gps_averages001_10_array, colAve_gps_averages001_1_array, colAve_gps_averages0018_10_array, ylabel_gps_ave, title_gps_ave, tables)
    # variances
    ylabel_gps_var = "gps_residual_variances"
    title_gps_var = "gps indicators: residuals variances"
    drawBar_gps(colVar_gps_averages1_25_array, colVar_gps_averages02_18_array, colVar_gps_averages001_10_array, colVar_gps_averages001_1_array, colVar_gps_averages0018_10_array, ylabel_gps_var, title_gps_var, tables)

    # osm
    tables = ['RAR', 'RARO', 'RDR', 'RDRO']
    # averages
    ylabel_osm_ave = "osm_residual_averages(degree degree meter meter)"
    title_osm_ave = "osm indicators: residuals averages"
    drawBar_osm(colAve_osm_averages1_25_array, colAve_osm_averages02_18_array, colAve_osm_averages001_10_array,
                colAve_osm_averages001_1_array, colAve_osm_averages0018_10_array, ylabel_osm_ave, title_osm_ave, tables)
    # variances
    ylabel_osm_var = "osm_residual_variances"
    title_osm_var = "osm indicators: residuals variances"
    drawBar_osm(colVar_osm_averages1_25_array, colVar_osm_averages02_18_array, colVar_osm_averages001_10_array,
                colVar_osm_averages001_1_array, colVar_osm_averages0018_10_array, ylabel_osm_var, title_osm_var, tables)

    plt.show()