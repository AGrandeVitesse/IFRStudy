BEGIN{FS=","}
{
	year =  substr($3,1,4)
	dp_depression = $4 - $5
	total_count[year]++
	if ($10 == 1){
		vis_count[year]++}
	if ($11 == 1){
		ceiling_count[year]++}
	if ($10 == 1 && $11 == 1){
		both_count[year]++}
	if ($10 == 1 || $11 == 1){
		total_ifr_count[year]++}
	if (dp_depression < 3.0){
		low_dpd[year]++}
}
END{
	for (year in total_count){
	  	vis_hours = 8760*vis_count[year]/total_count[year]
		clg_hours = 8760*ceiling_count[year]/total_count[year]
		both_hours = 8760*both_count[year]/total_count[year]
		ifr_hours = 8760*total_ifr_count[year]/total_count[year]
		dpd_hours = 8760*low_dpd[year]/total_count[year]
	    printf "%s,%.2f,%.2f,%.2f,%.2f,%.2f\n", year, vis_hours, both_hours, clg_hours, ifr_hours, dpd_hours
	}
}
