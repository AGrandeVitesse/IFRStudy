import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})
from scipy import stats

infile = '/home/scotts/ceiling/data/ifr_counts/hourly_ifr_counts.csv'
fig = plt.figure(figsize=[15,10])
early_counts = {}
mid_counts = {}
late_counts = {}
for line in open(infile).readlines():
    hour, early, mid, late = line.split(",")[1:]
    hour = int(hour)
    if hour not in early_counts:
        early_counts.update({hour: []})
        mid_counts.update({hour: []})
        late_counts.update({hour: []})
    early_counts[hour].append(int(early))
    mid_counts[hour].append(int(mid))
    late_counts[hour].append(int(late))
hour = sorted(early_counts.keys())
early_mean = [np.mean(early_counts[x]) for x in sorted(early_counts)]
mid_mean = [np.mean(mid_counts[x]) for x in sorted(mid_counts)]
late_mean = [np.mean(late_counts[x]) for x in sorted(late_counts)]
x = hour
y1 = early_mean
y2 = mid_mean
y3 = late_mean
plt.plot(x, y1, lw=3, color='blue', label='1973-1975') 
plt.plot(x, y2, lw=3, color='red', label='1994-1996') 
plt.plot(x, y3, lw=3, color='orange', label='2015-2017') 
plt.legend()
plt.xlabel('Hour (LST)')
plt.ylabel('IFR Days Per Year')
plt.savefig('/home/scotts/ceiling/plots/figure_3.png', format='png')
plt.savefig('/home/scotts/ceiling/plots/figure_3.eps', format='eps')
plt.show()
