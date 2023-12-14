def softuni_students(*args, **kwargs):
    students = args
    courses = kwargs
    student_courses = {student:courses[course] for course, student in students if courses.get(course, None)}
    student_courses = dict(sorted(student_courses.items(), key=lambda x: x[0]))
    res = [f"*** A student with the username {student} has successfully finished the course {course}!" for student, course in student_courses.items()]
    invalid_students = sorted(student for student in (s for i,s in students) if student not in student_courses)
    if invalid_students:
        res.append(f"!!! Invalid course students: {', '.join(invalid_students)}")
    return '\n'.join(res)

print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print()
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print()
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))