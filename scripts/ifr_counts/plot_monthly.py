import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 18})
from scipy import stats

infile = '/home/scotts/ceiling/data/ifr_counts/monthly_ifr_counts.csv'
fig = plt.figure(figsize=[15,10])
early_counts = {}
mid_counts = {}
late_counts = {}
for line in open(infile).readlines():
    month, early, mid, late = line.split(",")[1:]
    month = int(month)
    if month not in early_counts:
        early_counts.update({month: []})
        mid_counts.update({month: []})
        late_counts.update({month: []})
    early_counts[month].append(int(early))
    mid_counts[month].append(int(mid))
    late_counts[month].append(int(late))
month = sorted(early_counts.keys())
early_mean = [np.mean(early_counts[x]) for x in sorted(early_counts)]
mid_mean = [np.mean(mid_counts[x]) for x in sorted(mid_counts)]
late_mean = [np.mean(late_counts[x]) for x in sorted(late_counts)]
x = month
y1 = early_mean
y2 = mid_mean
y3 = late_mean
plt.plot(x, y1, lw=3, color='blue', label='1973-1975') 
plt.plot(x, y2, lw=3, color='red', label='1994-1996') 
plt.plot(x, y3, lw=3, color='orange', label='2015-2017') 
plt.legend()
plt.xlabel('Month')
plt.xticks(range(1,13), ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
plt.ylabel('Average IFR Hours Per Year')
plt.savefig('/home/scotts/ceiling/plots/figure_4.png', format='png')
plt.savefig('/home/scotts/ceiling/plots/figure_4.eps', format='eps')
plt.show()
