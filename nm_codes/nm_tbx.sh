#!/bin/bash

# Developed by Sameera K. Abeykoon (December 11th 2018)

# This will run the Neuromelanin data processing 

# If not subject numbers provided 
if [ "$#" -eq  "0" ]
   then
     echo Enter the Subject number
     read -a sub_num
     echo "Subject No: ${sub_num[@]}"
else
     # Get the subject numbers
     sub_num=$1
fi

#echo Enter the Subject number
#read -a sub_num
#echo "Subject No: ${sub_num[@]}"

# change the directory to NM folders
cd '/mnt/hcp01/nm_data/NM_toolbox'

echo "NM Data processing "
for s_num in "${sub_num[@]}";
do
        echo "NM data processing for ${s_num} "
        cp par_cp.m par.m
        replace "Subject_number" "${s_num}" -- par.m
	# run the NM_toolbox
        matlab -nodisplay -r "batch_run; quit"
done
