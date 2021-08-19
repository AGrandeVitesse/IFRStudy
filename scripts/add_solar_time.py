import datetime
import sys
station_file = '/home/scotts/ceiling/data/station_list.csv'
station_data = open(station_file).readlines()
for station_line in station_data:
    id, city, lat, lon = station_line.split(",")
    offset = float(lon)/15.0
    infile = '/home/scotts/ceiling/data/processed/%s.csv' % id
    outfile = '/home/scotts/ceiling/data/processed_new/%s.csv' % id
    out = open(outfile, 'w')
    data = open(infile).readlines()
    for data_line in data:
        date = data_line.split(",")[1]
        date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
        solar_date = date + datetime.timedelta(hours = offset)
        if solar_date.year < 1973:
            continue
        solar_time = solar_date.strftime("%Y%m%d-%H%M")
        line = "%s,%s" % (solar_time, data_line)
        out.write(line)
    out.close()
