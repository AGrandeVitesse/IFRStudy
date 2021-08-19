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
        hour = date[9:11]
        vis_flag = float(data_line.split(",")[9])
        ceil_flag = float(data_line.split(",")[10])
        if int(year) >= 1973 and int(year) <= 1975:
            if hour not in total_count_early:
                total_count_early.update({hour: 1.})
                ifr_count_early.update({hour: 0.})
            else:
                total_count_early[hour] += 1
            if vis_flag == 1 or ceil_flag == 1:
                ifr_count_early[hour] += 1
        if int(year) >= 1994 and int(year) <= 1996:
            if hour not in total_count_mid:
                total_count_mid.update({hour: 1.})
                ifr_count_mid.update({hour: 0.})
            else:
                total_count_mid[hour] += 1
            if vis_flag == 1 or ceil_flag == 1:
                ifr_count_mid[hour] += 1
        if int(year) >= 2015 and int(year) <= 2017:
            if hour not in total_count_late:
                total_count_late.update({hour: 1.})
                ifr_count_late.update({hour: 0.})
            else:
                total_count_late[hour] += 1
            if vis_flag == 1 or ceil_flag == 1:
                ifr_count_late[hour] += 1
    for hour in sorted(total_count_early):
        ifr_early_pct = ifr_count_early[hour] / total_count_early[hour]
        ifr_mid_pct = ifr_count_mid[hour] / total_count_mid[hour]
        ifr_late_pct = ifr_count_late[hour] / total_count_late[hour]
        print "%s,%s,%i,%i,%i" % (station, hour, 365*ifr_early_pct, 365*ifr_mid_pct, 365*ifr_late_pct)
