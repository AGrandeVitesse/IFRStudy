station_list = '/home/scotts/ceiling/data/station_list.csv'

for station_line in open(station_list).readlines():
    ifr_count_early = {}
    total_count_early = {}
    ifr_count_mid = {}
    total_count_mid = {}
    ifr_count_late = {}
    total_count_late = {}
    station = station_line.split(",")[0]
    infile = '/home/scotts/ceiling/data/processed/sites/{station}.csv'.format(station=station)
    for data_line in open(infile).readlines():
        date = data_line.split(",")[0]
        year = date[0:4]
        month = date[4:6]
        vis_flag = float(data_line.split(",")[9])
        ceil_flag = float(data_line.split(",")[10])
        if int(year) >= 1973 and int(year) <= 1975:
            if month not in total_count_early:
                total_count_early.update({month: 1.})
                ifr_count_early.update({month: 0.})
            else:
                total_count_early[month] += 1
            if vis_flag == 1 or ceil_flag == 1:
                ifr_count_early[month] += 1
        if int(year) >= 1994 and int(year) <= 1996:
            if month not in total_count_mid:
                total_count_mid.update({month: 1.})
                ifr_count_mid.update({month: 0.})
            else:
                total_count_mid[month] += 1
            if vis_flag == 1 or ceil_flag == 1:
                ifr_count_mid[month] += 1
        if int(year) >= 2015 and int(year) <= 2017:
            if month not in total_count_late:
                total_count_late.update({month: 1.})
                ifr_count_late.update({month: 0.})
            else:
                total_count_late[month] += 1
            if vis_flag == 1 or ceil_flag == 1:
                ifr_count_late[month] += 1
    for month in sorted(total_count_early):
        ifr_early_pct = ifr_count_early[month] / total_count_early[month]
        ifr_mid_pct = ifr_count_mid[month] / total_count_mid[month]
        ifr_late_pct = ifr_count_late[month] / total_count_late[month]
        print "%s,%s,%i,%i,%i" % (station, month, 720*ifr_early_pct, 720*ifr_mid_pct, 720*ifr_late_pct)
