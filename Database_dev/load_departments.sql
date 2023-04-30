.system echo "Inside script <load_departments.sql>"
.system echo "------------------------------------"
.mode csv
.import ./data_departments.csv departments
.mode list