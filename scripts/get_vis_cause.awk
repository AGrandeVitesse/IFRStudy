BEGIN{FS=","}
{
	date = $2
	for (i=5; i<=NF; i++){
		if ($i ~ "SM"){
			vis = substr($i,1,length($i)-2)
			if (vis+0 <= 6){
			  cause=$(i+1)
			  if (length(cause) > 7){
				cause=$(i+2)
			  }
			  printf "%s,%s,%s\n", date, vis, cause
			}
		}
	}
}
