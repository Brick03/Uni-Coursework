.system cls
.system echo "Inside script <top-level.sql>"
.system echo "-----------------------------"
--
.system echo "Switching the foreign keys ON/OFF"

-- If you have problems with legacy data in your database,
-- as a result of not cascading deletes in child tables,
-- then you can turn foreign_keys to OFF and call this script 
-- a few times to ensure that your code drops tables appropiately.
-- Make sure to turn it ON again though, to ensure your keys are 
-- doing what they are there for.

PRAGMA foreign_keys = ON;
--
.system echo "1"
.read create_departments.sql
.system echo "2"
.read create_marks.sql
.system echo "3"
.read create_modules.sql
.system echo "4"
.read create_modules_teachers.sql
.system echo "5"
.read create_staff.sql
.system echo "6"
.read create_students.sql
.system echo "7"
.read load_departments.sql
.system echo "8"
.read load_modules.sql
.system echo "9"
.read load_staff.sql
.system echo "10"
.read load_students.sql
.system echo "11"
.read load_marks.sql
.system echo "12"
.read load_modules_teachers.sql

--
.system echo "13"
.read report.sql


-- .system echo "departments ........................"
-- SELECT * FROM departments;   
-- .system echo "modules ........................"
-- SELECT * FROM modules;   
-- .system echo "staff ........................"
-- SELECT * FROM staff;
-- .system echo "marks ........................"
-- SELECT * FROM marks;  
-- .system echo "modules_teachers ........................"     
-- SELECT * FROM module_teachers;
-- .system echo "students ........................"
-- SELECT * FROM students;

.read drop_all.sql

