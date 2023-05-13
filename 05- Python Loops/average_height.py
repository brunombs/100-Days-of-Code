students_heights = input("Input a list of students heights ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

total_height = 0
total_students = 0
for height in students_heights:
    total_height += height
    total_students += 1
print(round(total_height/total_students))
