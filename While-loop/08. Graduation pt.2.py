name = input()
clas = 1
year = 0
grade_sum = 0
while clas <= 12:
    year += 1
    grade = float(input())
    grade_sum += grade
    if grade < 4:
        break
    else:
        clas += 1
avg_grade = grade_sum / year
if clas < 12:
    print(f'{name} has been excluded at {clas} grade')
else:
    print(f'{name} graduated. Average grade: {avg_grade:.2f}')
