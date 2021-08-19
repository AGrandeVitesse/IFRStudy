BEGIN{FS=","}
{
	month = substr($3,6,2)
	hour  = substr($3,12,2)
	month_hour = sprintf("%s,%s", month, hour)
	count[month_hour]++
	if ($10 + $11 > 0){
		ifr[month_hour]++
	}
}
END{
	for (month_hour in count){
		printf "%s,%.4f\n", month_hour, ifr[month_hour]/count[month_hour]
	}
}
