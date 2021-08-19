BEGIN{FS=","}
{
	hour  = substr($1,10,2)
	month = substr($1,5,2)
	year  = substr($1,1,4)
	vis= $10
	ceiling = $11
	total++
	if (vis + ceiling > 0){
		ifr++
	}
}
END{
	print substr(FILENAME,1,3), ifr/total}
