import numpy as np
import matplotlib.pyplot as plt
import sys, os, glob
from scipy import stats

station_list = '/home/scotts/ceiling/data/station_list.csv'
for line in open(station_list).readlines():
    id, name, lat, lon = line.rstrip().split(",") 
    infile = '/home/scotts/ceiling/data/ifr_counts/annual/%s.csv' % id
    year, vis, both, ceiling, total, low_dpd = np.genfromtxt(infile, delimiter=",", unpack=True)
    x = year
    y = total 
    m, b, m_min, m_max = stats.theilslopes(y,x)
    k, p = stats.kendalltau(x,y)
#    plt.plot(x,y)
#    plt.savefig('/home/scotts/ceiling/plots/timeseries/ceiling/%s.png' % id)
#    plt.close()
    print "%s,%.3f,%.3f,%.3f,%.3f,%.3f" % (id, m, b, m_min, m_max, p)
