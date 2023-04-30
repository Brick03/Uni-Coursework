.system echo "Inside script <load_modules.sql>"
.system echo "--------------------------------"
.mode csv
.import ./data_modules.csv modules
.mode list