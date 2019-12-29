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

def drawBar_gps(gps1, gps02, gps0018, gps001, ylabel, title, tables):
    n_groups = 6
    plt.figure()
    index = np.arange(n_groups)
    bar_width = 0.2
    opacity = 0.9
    bar1 = plt.bar(index, gps1, bar_width, alpha=opacity, color='b', label='$\sigma_{osm-ang}=1, \sigma_{osm-dis}=18$')
    bar2 = plt.bar(index + bar_width, gps02, bar_width, alpha=opacity, color='g', label='$\sigma_{osm-ang}=0.2, \sigma_{osm-dis}=18$')
    bar3 = plt.bar(index + bar_width*2, gps0018, bar_width, alpha=opacity, color='y', label='$\sigma_{osm-ang}=0.018, \sigma_{osm-dis}=18$')
    bar4 = plt.bar(index + bar_width*3, gps001, bar_width, alpha=opacity, color='r', label='$\sigma_{osm-ang}=0.01, \sigma_{osm-dis}=18$')
    plt.xlabel('gps residuals comparison at each direction')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks()
    plt.xticks(index + bar_width, tables)
    plt.legend()
    plt.savefig(dataPath[:-4] + "/" + ylabel + "-ang")

def drawBar_osm(osm1, osm02, osm0018, osm001, ylabel, title, tables):
    n_groups = 4
    plt.figure()
    index = np.arange(n_groups)
    bar_width = 0.2
    opacity = 0.9
    plt.bar(index, osm1, bar_width, alpha=opacity, color='b', label='$\sigma_{osm-ang}=1, \sigma_{osm-dis}=18$')
    plt.bar(index + bar_width, osm02, bar_width, alpha=opacity, color='g', label='$\sigma_{osm-ang}=0.2, \sigma_{osm-dis}=18$')
    plt.bar(index + bar_width*2, osm0018, bar_width, alpha=opacity, color='y', label='$\sigma_{osm-ang}=0.018, \sigma_{osm-dis}=18$')
    plt.bar(index + bar_width*3, osm001, bar_width, alpha=opacity, color='r', label='$\sigma_{osm-ang}=0.01, \sigma_{osm-dis}=18$')
    plt.xlabel('osm residuals comparison at relative angle and relative distance')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks()
    plt.xticks(index + bar_width, tables)
    plt.legend()
    plt.savefig(dataPath[:-4] + "/" + ylabel + "-ang")

if __name__=="__main__":
    dataPath = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/forSigma/data"

    # 1-18
    gps_averages1 = []
    gps_variances1 = []
    osm_averages1 = []
    osm_variances1 = []
    getData(dataPath, gps_averages1, gps_variances1, osm_averages1, osm_variances1, "0402_Sigma-ori-1-18-dis")
    colAve_gps_averages1_array = np.zeros(shape=6)
    colVar_gps_averages1_array = np.zeros(shape=6)
    colAve_gps_variances1_array = np.zeros(shape=6)
    colVar_gps_variances1_array = np.zeros(shape=6)
    colAve_osm_averages1_array = np.zeros(shape=4)
    colVar_osm_averages1_array = np.zeros(shape=4)
    colAve_osm_variances1_array = np.zeros(shape=4)
    colVar_osm_variances1_array = np.zeros(shape=4)
    dataProcess(gps_averages1, gps_variances1, osm_averages1, osm_variances1,  \
                colAve_gps_averages1_array, colVar_gps_averages1_array, colAve_gps_variances1_array, colVar_gps_variances1_array, \
                colAve_osm_averages1_array, colVar_osm_averages1_array, colAve_osm_variances1_array, colVar_osm_variances1_array)

    # 02-18
    gps_averages02 = []
    gps_variances02 = []
    osm_averages02 = []
    osm_variances02 = []
    getData(dataPath, gps_averages02, gps_variances02, osm_averages02, osm_variances02, "0402_Sigma-ori-02-18-dis")
    colAve_gps_averages02_array = np.zeros(shape=6)
    colVar_gps_averages02_array = np.zeros(shape=6)
    colAve_gps_variances02_array = np.zeros(shape=6)
    colVar_gps_variances02_array = np.zeros(shape=6)
    colAve_osm_averages02_array = np.zeros(shape=4)
    colVar_osm_averages02_array = np.zeros(shape=4)
    colAve_osm_variances02_array = np.zeros(shape=4)
    colVar_osm_variances02_array = np.zeros(shape=4)
    dataProcess(gps_averages02, gps_variances02, osm_averages02, osm_variances02,  \
                colAve_gps_averages02_array, colVar_gps_averages02_array, colAve_gps_variances02_array, colVar_gps_variances02_array, \
                colAve_osm_averages02_array, colVar_osm_averages02_array, colAve_osm_variances02_array, colVar_osm_variances02_array)

    # 0018-18
    gps_averages0018 = []
    gps_variances0018 = []
    osm_averages0018 = []
    osm_variances0018 = []
    getData(dataPath, gps_averages0018, gps_variances0018, osm_averages0018, osm_variances0018, "0402_Sigma-ori-0018-18-dis")
    colAve_gps_averages0018_array = np.zeros(shape=6)
    colVar_gps_averages0018_array = np.zeros(shape=6)
    colAve_gps_variances0018_array = np.zeros(shape=6)
    colVar_gps_variances0018_array = np.zeros(shape=6)
    colAve_osm_averages0018_array = np.zeros(shape=4)
    colVar_osm_averages0018_array = np.zeros(shape=4)
    colAve_osm_variances0018_array = np.zeros(shape=4)
    colVar_osm_variances0018_array = np.zeros(shape=4)
    dataProcess(gps_averages0018, gps_variances0018, osm_averages0018, osm_variances0018,  \
                colAve_gps_averages0018_array, colVar_gps_averages0018_array, colAve_gps_variances0018_array, colVar_gps_variances0018_array, \
                colAve_osm_averages0018_array, colVar_osm_averages0018_array, colAve_osm_variances0018_array, colVar_osm_variances0018_array)

    # 001-18
    gps_averages001 = []
    gps_variances001 = []
    osm_averages001 = []
    osm_variances001 = []
    getData(dataPath, gps_averages001, gps_variances001, osm_averages001, osm_variances001, "0402_Sigma-ori-001-18-dis")
    colAve_gps_averages001_array = np.zeros(shape=6)
    colVar_gps_averages001_array = np.zeros(shape=6)
    colAve_gps_variances001_array = np.zeros(shape=6)
    colVar_gps_variances001_array = np.zeros(shape=6)
    colAve_osm_averages001_array = np.zeros(shape=4)
    colVar_osm_averages001_array = np.zeros(shape=4)
    colAve_osm_variances001_array = np.zeros(shape=4)
    colVar_osm_variances001_array = np.zeros(shape=4)
    dataProcess(gps_averages001, gps_variances001, osm_averages001, osm_variances001,  \
                colAve_gps_averages001_array, colVar_gps_averages001_array, colAve_gps_variances001_array, colVar_gps_variances001_array, \
                colAve_osm_averages001_array, colVar_osm_averages001_array, colAve_osm_variances001_array, colVar_osm_variances001_array)


    # draw
    # gps
    tables = ['ER', 'ERO', 'NR', 'NRO', 'UR', 'URO']
    # averages
    ylabel_gps_ave = "gps_residual_averages(meter)"
    title_gps_ave = "gps indicators: residuals averages when $\sigma_{osm-dis}$ is fixed"
    drawBar_gps(colAve_gps_averages1_array, colAve_gps_averages02_array, colAve_gps_averages0018_array, colAve_gps_averages001_array, ylabel_gps_ave, title_gps_ave, tables)
    # variances
    ylabel_gps_var = "gps_residual_variances"
    title_gps_var = "gps indicators: residuals variances when $\sigma_{osm-dis}$ is fixed"
    drawBar_gps(colVar_gps_averages1_array, colVar_gps_averages02_array, colVar_gps_averages0018_array, colVar_gps_averages001_array, ylabel_gps_var, title_gps_var, tables)

    # osm
    tables = ['RAR', 'RARO', 'RDR', 'RDRO']
    # averages
    ylabel_osm_ave = "osm_residual_averages(degree degree meter meter)"
    title_osm_ave = "osm indicators: residuals averages when $\sigma_{osm-dis}$ is fixed"
    drawBar_osm(colAve_osm_averages1_array, colAve_osm_averages02_array, colAve_osm_averages0018_array,
                colAve_osm_averages001_array, ylabel_osm_ave, title_osm_ave, tables)
    # variances
    ylabel_osm_var = "osm_residual_variances"
    title_osm_var = "osm indicators: residuals variances when $\sigma_{osm-dis}$ is fixed"
    drawBar_osm(colVar_osm_averages1_array, colVar_osm_averages02_array, colVar_osm_averages0018_array,
                colVar_osm_averages001_array, ylabel_osm_var, title_osm_var, tables)

    plt.show()