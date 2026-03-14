#v_students_active EJERCICIO_1
CREATE OR REPLACE VIEW v_students_active AS
	SELECT 
		s.student_id, 
		s.doc_type, 
		s.doc_number, 
		CONCAT(first_name, ' ', last_name) AS Full_Name,
		s.status, 
		s.created_at,
		p.name AS program
	FROM students s
	INNER JOIN student_programs sp ON s.student_id = sp.student_id
	INNER JOIN programs p ON sp.program_id = p.program_id
	WHERE s.status = 'ACTIVE';
SELECT * FROM v_students_active;
#v_teachers_departments EJERCICIO_2
CREATE OR REPLACE VIEW v_teachers_departments AS
	SELECT 
		t.teacher_id, 
        t.full_name, 
        t.email, 
        t.status,
        d.name AS department
	FROM teachers t
	INNER JOIN departments d ON t.dept_id = d.dept_id
	WHERE t.status = 'ACTIVE';
SELECT * FROM v_teachers_departments;
#v_sections_periods EJERCICIO_3
CREATE OR REPLACE VIEW v_sections_periods AS
    SELECT 
		cs.section_id, 
		c.code AS Courses_Code,
		c.name AS Courses_Name,
		p.name AS Program_Name,
		ap.code AS Period_Name,
		t.full_name AS Teacher_Name,
		group_code, 
		capacity, 
		needs_reassign, 
		created_at
	FROM course_sections cs
	INNER JOIN courses c ON cs.course_id = c.course_id
	INNER JOIN programs p ON c.program_id = p.program_id
	INNER JOIN academic_periods ap ON cs.period_id = ap.period_id
	INNER JOIN teachers t on cs.teacher_id = t.teacher_id
    WHERE ap.code = '2026-1';
SELECT * FROM v_sections_periods;
#v_courses_roster EJERCICIO_4
CREATE OR REPLACE VIEW v_courses_roster AS
	SELECT 
		e.section_id,
		c.code AS Courses_Code,
		c.name AS Courses_Name,
		cs.group_code AS Course_Group_Code,
		e.student_id,
		CONCAT(s.first_name, ' ', s.last_name) AS Student_Name,
		CONCAT(s.doc_type, ' ', s.doc_number) AS Student_Doc,
		enrollment_id
	FROM enrollments e 
	INNER JOIN course_sections cs ON e.section_id = cs.section_id
	INNER JOIN courses c ON cs.course_id = c.course_id
	INNER JOIN students s ON e.student_id = s.student_id;
	ORDER BY e.section_id, Student_Name;
SELECT * FROM v_courses_roster;
#v_assessment_sections EJERCICIO_5
CREATE OR REPLACE VIEW v_assessment_sections AS
	SELECT 
		cs.section_id,
		cs.group_code,
		c.name AS Course_Name,
		c.code AS Course_Code,
		a.name Evaluation_Name, 
		a.weight_pct
	FROM assessments a
	INNER JOIN course_sections cs ON a.section_id = cs.section_id
	INNER JOIN courses c ON cs.course_id = c.course_id
SELECT * FROM v_assessment_sections
#v_students_grades EJERCICIO_6
CREATE OR REPLACE VIEW v_students_grades AS
	SELECT 
		s.student_id, 
		CONCAT(s.doc_type, ' ', s.doc_number) AS Studen_Doc,
		CONCAT(s.first_name, ' ', s.last_name) AS Studen_Name, 
		a.name AS Assessment_Name,
		c.code AS Course_Code,
		g.score,
		g.graded_at,
		e.section_id
	FROM grades g
	INNER JOIN enrollments e ON g.enrollment_id = e.enrollment_id
	INNER JOIN assessments a ON g.assessment_id = a.assessment_id
	INNER JOIN students s ON e.student_id = s.student_id
    INNER JOIN course_sections cs ON a.section_id = cs.section_id
    INNER JOIN courses c ON cs.course_id = c.course_id
	ORDER BY e.section_id, s.student_id, a.assessment_id;
SELECT * FROM v_students_grades
#v_students_sum EJERCICIO_7
CREATE OR REPLACE VIEW v_students_sum AS
	SELECT 
		s.student_id, 
		CONCAT(s.doc_type, ' ', s.doc_number) AS Studen_Doc,
		CONCAT(s.first_name, ' ', s.last_name) AS Studen_Name, 
		c.code AS Course_Code,
		e.section_id,
		SUM(g.score * a.weight_pct / 100) AS weighted_score
	FROM grades g
	INNER JOIN enrollments e ON g.enrollment_id = e.enrollment_id
	INNER JOIN assessments a ON g.assessment_id = a.assessment_id
	INNER JOIN students s ON e.student_id = s.student_id
	INNER JOIN course_sections cs ON e.section_id = cs.section_id
	INNER JOIN courses c ON cs.course_id = c.course_id
	GROUP BY s.student_id, Studen_Name, Studen_Doc, c.code, e.section_id
	ORDER BY s.student_id;
SELECT * FROM v_students_sum;
#v_courses_sum EJERCICIO_8
CREATE OR REPLACE VIEW v_courses_sum AS
	SELECT 
		section_id,
		course_code,
		AVG(weighted_score) AS course_average
	FROM (SELECT
			c.code AS Course_Code,
			e.section_id,
			SUM(g.score * a.weight_pct / 100) AS weighted_score
		FROM grades g
		INNER JOIN enrollments e ON g.enrollment_id = e.enrollment_id
		INNER JOIN assessments a ON g.assessment_id = a.assessment_id
		INNER JOIN course_sections cs ON e.section_id = cs.section_id
		INNER JOIN courses c ON cs.course_id = c.course_id
		GROUP BY c.code, e.section_id, e.student_id) 
		AS student_final_scores
		GROUP BY section_id, course_code
		ORDER BY section_id;
SELECT * FROM v_courses_sum;
#v_courses_period EJERCICIO_9
CREATE OR REPLACE VIEW v_courses_period AS
	SELECT
		s.student_id,
		CONCAT(s.first_name, ' ', s.last_name) AS Studen_Name,
		CONCAT(s.doc_type, ' ', s.doc_number) AS Studen_Doc,
		c.code AS Course_Code,
		c.name AS Course_Name, 
		ap.code AS Period,
		p.name AS Career_Name,
		p.modality,
		p.level
	FROM enrollments e
	INNER JOIN students s ON e.student_id = s.student_id
	INNER JOIN course_sections cs ON e.section_id = cs.section_id
	INNER JOIN academic_periods ap ON cs.period_id = ap.period_id
	INNER JOIN courses c ON cs.course_id = c.course_id
	INNER JOIN programs p ON c.program_id = p.program_id
	WHERE c.code = 'BD101' AND ap.code = '2026-1'
	ORDER BY c.course_id;
SELECT * FROM v_courses_period;