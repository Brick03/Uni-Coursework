.system echo "Inside script <drop_all.sql>"
.system echo "--------------------------------"

PRAGMA foreign_keys = OFF;

DROP TABLE departments;     
DROP TABLE modules;          
DROP TABLE students;
DROP TABLE marks;           
DROP TABLE module_teachers;
DROP TABLE staff;