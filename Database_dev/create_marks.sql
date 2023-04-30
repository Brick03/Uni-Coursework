.system echo "Inside script <create_marks.sql>"
.system echo "--------------------------------"
DROP TABLE IF EXISTS marks;
CREATE TABLE marks(
mark_id INTEGER PRIMARY KEY,
student_id INTEGER,
subject_id INTEGER,
mark FLOAT,
FOREIGN KEY(student_id) 
	REFERENCES students(student_id),
FOREIGN KEY(subject_id) 
	REFERENCES modules(module_id));
