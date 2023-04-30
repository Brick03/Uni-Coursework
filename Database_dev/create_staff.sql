.system echo "Inside script <create_staff.sql>"
.system echo "--------------------------------"
DROP TABLE IF EXISTS staff;
CREATE TABLE staff(
staff_id INTEGER PRIMARY KEY,
fname TEXT,
sname TEXT,
email TEXT,
dept INTEGER,
FOREIGN KEY(dept) 
	REFERENCES departments(dept_id));