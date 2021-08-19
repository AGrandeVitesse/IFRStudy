BEGIN{FS=","}
{
	hour=substr($0,1,11)
	if (hour != current_hour){
		print current_line
	}
	current_line = $0
	current_hour = hour
}
END{
	print $0
}
