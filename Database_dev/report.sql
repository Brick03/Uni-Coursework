.system echo "Inside script <report.sql>"
.system echo "-----------------------------"

.system echo "-"
.system echo "List all columns from tables departments, modules, staff and modules_teachers tables(2)"
SELECT * 
FROM modules m
	JOIN module_teachers mt
		ON m.module_id=mt.subject_id
	JOIN staff s
		ON mt.teacher_id=s.staff_id
	JOIN departments d
		ON d.dept_id=s.dept;

.system echo "-"
.system echo "List the average marks for all marks (2)"
SELECT AVG(m.mark)
FROM marks m;

.system echo "-"
.system echo "List the first name, surname and email of staff, ordered by e-mail, but only list 10 of the staff (4)"
SELECT s.fname, s.sname, s.email
FROM staff s
ORDER BY s.email ASC
LIMIT 10;

.system echo "-"
.system echo "List the forename and surname of the student and their marks per module 8"
SELECT s.fname, s.sname,
	group_concat(m.mark)
FROM students s
	 JOIN marks m
		ON s.student_id=m.student_id
GROUP BY s.fname;

.system echo "-"
.system echo "List the title of a subject and the average mark obtained for that subject and order the output from highest to lowest mark 6"
SELECT md.title, AVG(mk.mark)
FROM modules md
	JOIN marks mk
		ON md.module_id=mk.subject_id
GROUP BY md.title
ORDER BY 2 DESC;
