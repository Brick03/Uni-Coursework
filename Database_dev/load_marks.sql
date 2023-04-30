.system echo "Inside script <load_marks.sql>"
.system echo "------------------------------"
.mode csv
.import ./data_marks.csv marks
.mode list