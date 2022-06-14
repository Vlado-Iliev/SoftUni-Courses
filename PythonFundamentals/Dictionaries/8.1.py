def finish(courses):
    for key,value in courses.items():
        print(f'{key}: {len(value)}')
        for student in range(0,len(value)):
            print(f'-- {courses[key][student]}')


courses = dict()

while True:
    line = input()
    if line == 'end':
        finish(courses)
        break

    command = line.split(' : ')
    course = command[0]
    name = command[1]

    if course in courses.keys():
        courses[course].append(name)
    else:
        courses[course] = list()
        courses[course].append(name)

