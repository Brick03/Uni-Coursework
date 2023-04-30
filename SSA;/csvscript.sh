#!/bin/bash 

cat StudentList.csv | cut -d, -f 4 >1.csv

cat 1.csv | cut -c 1-9 > output.csv 

tr [A-Z] [a-z] < output.csv > column1.csv 

cat StudentList.csv | cut -d, -f 4 > column2.csv 

cat StudentList.csv | awk -F ',' '{print $3}' > output2.csv

tr -d [:punct:] < output2.csv > column3.csv

cat StudentList.csv | awk -F ',' '{print $2}' > output3.csv

tr -d [:punct:] < output3.csv > column4.csv

echo "RHNID, EMAIL, FIRSTNAME, LASTNAME" > redhat_upload.csv

past -d, column1.csv column2.csv column3.csv column4.csv >> redhat_upload.csv