data = int(input())

student_record = dict()

for n in range(data):
    name = input()
    grade = float(input())
    if name in student_record.keys():
        student_record[name][0] += grade
        student_record[name][1] += 1
    else:
        student_record[name] = list()
        student_record[name].append(grade)
        student_record[name].append(1)

for key,value in student_record.items():
    if value[0] / value[1] < 4.50:
        pass
    else:
        print(f'{key} -> {value[0] / value[1]:.2f}')