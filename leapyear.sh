#!/bin/bash
year=$1    #take argurment for year 
number_of_args=$# #takes number of args

if ! [ $number_of_args == 1 ] #checks number or args if not = to 1 it ends script
    then
    	echo "Usage: leapyear.sh <year>"
	exit 1		
fi
if ! [[ "$year" =~ ^[0-9]+$ ]] #checks if input is integer if not ends script
    then
    	echo "Usage: leapyear.sh <year>"
        exit 1
fi
if (( $year%4 == 0 )) #checks if year is divisable by 4 and if so sets check to true else sets to false
    then
        check=true
    else
        check=false
fi
if (( $year%100 == 0 )) #checks if year is divisable by 100 and if so sets check to false
    then
        check=false
fi
if (( $year%400 == 0 )) #checks if year is divisable by 400 and if so sets check to true
    then
        check=true
fi
if $check; #outputs result 
    then
	echo "true"
	echo "Leapyear!"
    else
	echo "false"
	echo "not a leapyear"
fi
