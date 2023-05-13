student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for aluno in student_scores:
    if student_scores[aluno] > 90:
        student_grades[aluno] = "Outstanding"
    elif student_scores[aluno] > 80 and student_scores[aluno] <= 90:
        student_grades[aluno] = "Exceeds expectations"
    elif student_scores[aluno] > 70 and student_scores[aluno] <= 80:
        student_grades[aluno] = "Acceptable"
    elif student_scores[aluno] <= 70:
        student_grades[aluno] = "Fail"

print(student_grades)