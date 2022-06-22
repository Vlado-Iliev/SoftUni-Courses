def average_grade(grades):
    total = sum(list(map(float, grades)))
    return total / len(grades)


n = int(input())

student_record = {}

for _ in range(n):
    name, grade = input().split(' ')
    if name not in student_record:
        student_record[name] = []
    student_record[name].append(grade)

for student, grades in student_record.items():
    print(f'{student} -> {" ".join(grades)} (avg: {average_grade(grades):.2f})')
