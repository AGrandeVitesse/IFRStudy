BEGIN{FS=","}
{
	vis_flag = 0
	cei_flag = 0
	if (NR==1){
		next}
	year =  substr($2,1,4)
	month = substr($2,6,2)
	hour  = substr($2,12,2)
	vis   = $6
	type  = $7
	hgt   = $8
	count++
	if (vis < 3){
		vis_flag = 1
	}
	if (type=="BKN"||type=="OVC"||type=="VV"){
		if (hgt < 1000){
			cei_flag = 1
		}
	}
	printf "%s,%s,%s,%s,%s,%s,%s,%s,%i,%i\n", $1, $2, $3, $4, $5, $6, $7, $8, vis_flag, cei_flag
}
