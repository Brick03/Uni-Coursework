.system echo "Inside script <load_students.sql>"
.system echo "---------------------------------"
.mode csv
.import ./data_students.csv students
.mode list