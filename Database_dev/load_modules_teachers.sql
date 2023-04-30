.system echo "Inside script <load_modules_teachers.sql>"
.system echo "-----------------------------------------"
.mode csv
.import ./data_modules_teachers.csv module_teachers
.mode list