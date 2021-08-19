import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})
from scipy import stats

infile = '/home/scotts/ceiling/data/ifr_counts/annual_ifr_counts.csv'
fig = plt.figure(figsize=[15,10])
vis_counts = {}
ceil_counts = {}
for line in open(infile).readlines():
    year, vis, ceil = line.split(",")[1:]
    year = int(year)
    if year not in vis_counts:
        vis_counts.update({year: []})
        ceil_counts.update({year: []})
    vis_counts[year].append(int(vis))
    ceil_counts[year].append(int(ceil))
year = sorted(vis_counts.keys())
vis_mean = [np.mean(vis_counts[x]) for x in sorted(vis_counts)]
vis_err = [np.std(vis_counts[x]) for x in sorted(vis_counts)]
ceil_mean = [np.mean(ceil_counts[x]) for x in sorted(ceil_counts)]
ceil_err = [np.std(ceil_counts[x]) for x in sorted(ceil_counts)]
x = year
y1 = vis_mean
m, b, m_min, m_max = stats.theilslopes(y1,x)
y1_pred = [m*i + b for i in x]
plt.plot(x, y1, lw=3, color='blue', label='Visibility') 
plt.plot(x, y1_pred, lw=1, color='blue')
y2 = ceil_mean
m, b, m_min, m_max = stats.theilslopes(y2,x)
y2_pred = [m*i + b for i in x]
plt.plot(x, y2, lw=3, color='red', label='Ceiling') 
plt.plot(x, y2_pred, lw=1, color='red')
plt.legend()
plt.xlabel('Year')
plt.ylabel('IFR Hours Per Year')
plt.savefig('/home/scotts/ceiling/plots/figure_5.png', format='png')
plt.savefig('/home/scotts/ceiling/plots/figure_5.eps', format='eps')
plt.show()
