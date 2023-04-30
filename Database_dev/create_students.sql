.system echo "Inside script <create_students.sql>"
.system echo "----------------------------------"
DROP TABLE IF EXISTS students;
CREATE TABLE students(
student_id INTEGER PRIMARY KEY,
fname TEXT,
sname TEXT,
email TEXT,
dept INTEGER,
FOREIGN KEY(dept) 
	REFERENCES departments(dept_id));