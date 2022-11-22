#!/bin/bash
year = $1

if [ $year%4 = 0 ]
    then
        c=1
    else
        c=0
fi
if [ $year%100 = 1]
    then
        c=0
fi
if [ $year%400 = 0]
    then
        c=1
fi
    