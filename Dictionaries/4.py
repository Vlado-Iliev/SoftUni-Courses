line = input()
school = dict()
while ":" in line:
    (name,id_number,course) = line.split(':')


    if course not in school.keys():
        school[course] = dict()

    school[course][id_number] = name

    line = input()

line = line.replace('_'," ")

for id_number in school[line]:
    print(f'{school[line][id_number]} - {id_number}')