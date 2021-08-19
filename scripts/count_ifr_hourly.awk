BEGIN{FS=","}
{
	hour  = substr($1,10,2)
	total_count[hour]++
	if ($10 == 1){
		vis_count[hour]++}
	if ($11 == 1){
		ceiling_count[hour]++}
	if ($10 == 1 && $11 == 1){
		both_count[hour]++}
	if ($10 == 1 || $11 == 1){
		total_ifr_count[hour]++}
}
END{
	for (hour in total_count){
	  	vis_hours = vis_count[hour]/total_count[hour]
		clg_hours = ceiling_count[hour]/total_count[hour]
		both_hours = both_count[hour]/total_count[hour]
		ifr_hours = total_ifr_count[hour]/total_count[hour]
	    printf "%s,%.4f,%.4f,%.4f,%.4f\n", hour, vis_hours, both_hours, clg_hours, ifr_hours
	}
}
