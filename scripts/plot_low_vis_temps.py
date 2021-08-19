import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 21})

early_file = '/home/scotts/ceiling/data/low_vis_temps/low_vis_temps_early.dat'
mid_file = '/home/scotts/ceiling/data/low_vis_temps/low_vis_temps_mid.dat'
late_file = '/home/scotts/ceiling/data/low_vis_temps/low_vis_temps_late.dat'
early_data = np.genfromtxt(early_file)
mid_data = np.genfromtxt(mid_file)
late_data = np.genfromtxt(late_file)
total_early = len(early_data)
total_mid   = len(mid_data)
total_late  = len(late_data)
x = np.arange(-10,31, 0.5)
y_early = []
y_mid   = []
y_late  = []
for xi in x:
    y_early.append(float(len([i for i in early_data if i < xi]))/total_early)
    y_mid.append(float(len([i for i in mid_data if i < xi]))/total_mid)
    y_late.append(float(len([i for i in late_data if i < xi]))/total_late)

fig = plt.figure(figsize=[15,10])
plt.plot(x, y_early, lw=3, color='blue', label='1973-1975')
plt.plot(x, y_mid, lw=3, color='red', label='1994-1996')
plt.plot(x, y_late, lw=3, color='orange', label='2015-2017')
plt.legend()
plt.xlabel('Temperature (C)')
plt.ylabel('Cumulative Distribution')
plt.savefig('/home/scotts/ceiling/plots/figure_6.png', format='png')
plt.savefig('/home/scotts/ceiling/plots/figure_6.eps', format='eps')
plt.show()
