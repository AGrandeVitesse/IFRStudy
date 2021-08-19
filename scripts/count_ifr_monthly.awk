BEGIN{FS=","}
{
	month = substr($1,5,2)
	total_count[month]++
	if ($10 == 1){
		vis_count[month]++}
	if ($11 == 1){
		ceiling_count[month]++}
	if ($10 == 1 && $11 == 1){
		both_count[month]++}
	if ($10 == 1 || $11 == 1){
		total_ifr_count[month]++}
}
END{
	for (month in total_count){
	  	vis_hours = vis_count[month]/total_count[month]
		clg_hours = ceiling_count[month]/total_count[month]
		both_hours = both_count[month]/total_count[month]
		ifr_hours = total_ifr_count[month]/total_count[month]
	    printf "%s,%.4f,%.4f,%.4f,%.4f\n", month, vis_hours, both_hours, clg_hours, ifr_hours
	}
}
