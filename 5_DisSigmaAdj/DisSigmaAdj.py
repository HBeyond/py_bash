# this code is for the average and variance calculation in the experience where
# the dis sigma changes but ang sigma fixed

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

def drawBar_gps(gps18, gps10, gps1, ylabel, title, tables):
    n_groups = 6
    plt.figure()
    index = np.arange(n_groups)
    bar_width = 0.3
    opacity = 0.9
    plt.bar(index, gps18, bar_width, alpha=opacity, color='b', label='$\sigma_{osm-ang}=0.2, \sigma_{osm-dis}=18$')
    plt.bar(index + bar_width, gps10, bar_width, alpha=opacity, color='g', label='$\sigma_{osm-ang}=0.2, \sigma_{osm-dis}=10$')
    plt.bar(index + bar_width*2, gps1, bar_width, alpha=opacity, color='y', label='$\sigma_{osm-ang}=0.2, \sigma_{osm-dis}=1$')
    plt.xlabel('residuals')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks()
    plt.xticks(index + bar_width, tables)
    plt.legend()
    plt.savefig(dataPath[:-4] + "/" + ylabel + "-dis")

def drawBar_osm(osm18, osm10, osm1, ylabel, title, tables):
    n_groups = 4
    plt.figure()
    index = np.arange(n_groups)
    bar_width = 0.210
    opacity = 0.9
    plt.bar(index, osm18, bar_width, alpha=opacity, color='b', label='$\sigma_{osm-ang}=0.2, \sigma_{osm-dis}=18$')
    plt.bar(index + bar_width, osm10, bar_width, alpha=opacity, color='g', label='$\sigma_{osm-ang}=0.2, \sigma_{osm-dis}=10$')
    plt.bar(index + bar_width*2, osm1, bar_width, alpha=opacity, color='y', label='$\sigma_{osm-ang}=0.2, \sigma_{osm-dis}=1$')
    plt.xlabel('osm residuals comparison at relative angle and relative distance')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks()
    plt.xticks(index + bar_width, tables)
    plt.legend()
    plt.savefig(dataPath[:-4] + "/" + ylabel + "-dis")

if __name__=="__main__":
    dataPath = "/Users/user/Desktop/mac-ubuntu-share/DriverLoggerData/forSigma/data"

    # 02-18
    gps_averages18 = []
    gps_variances18 = []
    osm_averages18 = []
    osm_variances18 = []
    getData(dataPath, gps_averages18, gps_variances18, osm_averages18, osm_variances18, "0402_Sigma-ori-02-18-dis")
    colAve_gps_averages18_array = np.zeros(shape=6)
    colVar_gps_averages18_array = np.zeros(shape=6)
    colAve_gps_variances18_array = np.zeros(shape=6)
    colVar_gps_variances18_array = np.zeros(shape=6)
    colAve_osm_averages18_array = np.zeros(shape=4)
    colVar_osm_averages18_array = np.zeros(shape=4)
    colAve_osm_variances18_array = np.zeros(shape=4)
    colVar_osm_variances18_array = np.zeros(shape=4)
    dataProcess(gps_averages18, gps_variances18, osm_averages18, osm_variances18, \
                colAve_gps_averages18_array, colVar_gps_averages18_array, colAve_gps_variances18_array,
                colVar_gps_variances18_array, \
                colAve_osm_averages18_array, colVar_osm_averages18_array, colAve_osm_variances18_array,
                colVar_osm_variances18_array)

    # 02-10
    gps_averages10 = []
    gps_variances10 = []
    osm_averages10 = []
    osm_variances10 = []
    getData(dataPath, gps_averages10, gps_variances10, osm_averages10, osm_variances10, "0402_Sigma-ori-02-10-dis")
    colAve_gps_averages10_array = np.zeros(shape=6)
    colVar_gps_averages10_array = np.zeros(shape=6)
    colAve_gps_variances10_array = np.zeros(shape=6)
    colVar_gps_variances10_array = np.zeros(shape=6)
    colAve_osm_averages10_array = np.zeros(shape=4)
    colVar_osm_averages10_array = np.zeros(shape=4)
    colAve_osm_variances10_array = np.zeros(shape=4)
    colVar_osm_variances10_array = np.zeros(shape=4)
    dataProcess(gps_averages10, gps_variances10, osm_averages10, osm_variances10, \
                colAve_gps_averages10_array, colVar_gps_averages10_array, colAve_gps_variances10_array,
                colVar_gps_variances10_array, \
                colAve_osm_averages10_array, colVar_osm_averages10_array, colAve_osm_variances10_array,
                colVar_osm_variances10_array)

    # 02-1
    gps_averages1 = []
    gps_variances1 = []
    osm_averages1 = []
    osm_variances1 = []
    getData(dataPath, gps_averages1, gps_variances1, osm_averages1, osm_variances1, "0402_Sigma-ori-02-1-dis")
    colAve_gps_averages1_array = np.zeros(shape=6)
    colVar_gps_averages1_array = np.zeros(shape=6)
    colAve_gps_variances1_array = np.zeros(shape=6)
    colVar_gps_variances1_array = np.zeros(shape=6)
    colAve_osm_averages1_array = np.zeros(shape=4)
    colVar_osm_averages1_array = np.zeros(shape=4)
    colAve_osm_variances1_array = np.zeros(shape=4)
    colVar_osm_variances1_array = np.zeros(shape=4)
    dataProcess(gps_averages1, gps_variances1, osm_averages1, osm_variances1, \
                colAve_gps_averages1_array, colVar_gps_averages1_array, colAve_gps_variances1_array,
                colVar_gps_variances1_array, \
                colAve_osm_averages1_array, colVar_osm_averages1_array, colAve_osm_variances1_array,
                colVar_osm_variances1_array)

    # draw
    # gps
    tables = ['ER', 'ERO', 'NR', 'NRO', 'UR', 'URO']
    # averages
    ylabel_gps_ave = "gps_residual_averages(meter)"
    title_gps_ave = "gps indicators: residuals averages when $\sigma_{osm-ang}$ is fixed"
    drawBar_gps(colAve_gps_averages18_array, colAve_gps_averages10_array, colAve_gps_averages1_array, ylabel_gps_ave, title_gps_ave, tables)
    # variances
    ylabel_gps_var = "gps_residual_variances"
    title_gps_var = "gps indicators: residuals variances when $\sigma_{osm-ang}$ is fixed"
    drawBar_gps(colVar_gps_averages18_array, colVar_gps_averages10_array, colVar_gps_averages1_array, ylabel_gps_var, title_gps_var, tables)

    # osm
    tables = ['RAR', 'RARO', 'RDR', 'RDRO']
    # averages
    ylabel_osm_ave = "osm_residual_averages(degree degree meter meter)"
    title_osm_ave = "osm indicators: residuals averages when $\sigma_{osm-ang}$ is fixed"
    drawBar_osm(colAve_osm_averages18_array, colAve_osm_averages10_array, colAve_osm_averages1_array,
                 ylabel_osm_ave, title_osm_ave, tables)
    # variances
    ylabel_osm_var = "osm_residual_variances"
    title_osm_var = "osm indicators: residuals variances when $\sigma_{osm-ang}$ is fixed"
    drawBar_osm(colVar_osm_averages18_array, colVar_osm_averages10_array, colVar_osm_averages1_array,
                 ylabel_osm_var, title_osm_var, tables)

    plt.show()