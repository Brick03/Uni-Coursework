#!/bin/bash
year=$1
number_of_args=$#

if ! [ $number_of_args == 1 ]
	then
		echo "Usage: leapyear.sh <year>"
		exit 1
		assert_success=false
	else
		assert_success=true
fi
if ! [[ "$year" =~ ^[0-9]+$ ]]
    then
    	echo "Usage: leapyear.sh <year>"
        exit 1
        assert_success=false
    else
    	assert_success=true
fi

if (( $year%4 == 0 ))
    then
        c=true
    else
        c=false
fi
if (( $year%100 == 0 ))
    then
        c=false
fi
if (( $year%400 == 0 ))
    then
        c=true
fi
if $c; 
	then
		echo "true"
	else
		echo "false"
fi
