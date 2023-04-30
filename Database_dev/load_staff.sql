.system echo "Inside script <load_staff.sql>"
.system echo "------------------------------"
.mode csv
.import ./data_staff.csv staff
.mode list