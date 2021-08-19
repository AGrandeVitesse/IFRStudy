station_list = '/home/scotts/ceiling/data/station_list.csv'

for station_line in open(station_list).readlines():
    vis_count = {}
    ceil_count = {}
    total_count = {}
    station = station_line.split(",")[0]
    infile = '/home/scotts/ceiling/data/processed/sites/{station}.csv'.format(station=station)
    for data_line in open(infile).readlines():
        date = data_line.split(",")[0]
        year = date[0:4]
        vis_flag = float(data_line.split(",")[9])
        ceil_flag = float(data_line.split(",")[10])
        if year not in total_count:
            total_count.update({year: 1.})
            vis_count.update({year: 0.})
            ceil_count.update({year: 0.})
        else:
            total_count[year] += 1
        if vis_flag == 1:
            vis_count[year] += 1
        if ceil_flag == 1:
            ceil_count[year] += 1
    for year in sorted(total_count):
        vis_pct = vis_count[year] / total_count[year]
        ceil_pct = ceil_count[year] / total_count[year]
        print "%s,%s,%i,%i" % (station, year, 8760*vis_pct, 8760*ceil_pct)
