#!/bin/bash

stl_full=/home/scotts/ceiling/data/filtered_data/STL_low_vis.csv
stl_vis=/home/scotts/ceiling/data/STL.vis

cat $stl_full | while read line; do
	cause="NA"
	vis_flag=`echo $line | cut -d, -f9`
	if [ $vis_flag -eq 1 ]; then
		date=`echo $line | cut -d, -f2`
		cause=`grep $date $stl_vis | cut -d, -f3`
	fi
	printf "%s,%s\n" $line $cause
done
