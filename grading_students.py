n = int(input())
grades = []
for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)
new_grades = []
for grade in grades:
    if grade < 38:
        print(grade)
    else:
        mode_grade = grade % 5
        if mode_grade < 3:
            print(grade)
        else:
            print((grade + (5 - mode_grade)))


