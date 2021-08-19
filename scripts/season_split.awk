BEGIN{FS=","}
{
	month = substr($1,5,2)
	if (month == "03" || month == "04" || month == "05"){
		print > "spring.csv"}
	if (month == "06" || month == "07" || month == "08"){
		print > "summer.csv"}
	if (month == "09" || month == "10" || month == "11"){
		print > "autumn.csv"}
	if (month == "12" || month == "01" || month == "02"){
		print > "winter.csv"}
}
