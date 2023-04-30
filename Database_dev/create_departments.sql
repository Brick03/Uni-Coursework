.system echo "Inside script <create_departments.sql>"
.system echo "--------------------------------------"
DROP TABLE IF EXISTS departments;
CREATE TABLE departments(
dept_id INTEGER PRIMARY KEY,
title TEXT);

