.system echo "Inside script <create_modules_teachers.sql>"
.system echo "-------------------------------------------"
DROP TABLE IF EXISTS module_teachers;
CREATE TABLE module_teachers(
subject_teachers_id INTEGER PRIMARY KEY,
subject_id INTEGER,
teacher_id INTEGER,
FOREIGN KEY(subject_id) 
	REFERENCES modules(module_id),
FOREIGN KEY(teacher_id) 
	REFERENCES staff(staff_id));