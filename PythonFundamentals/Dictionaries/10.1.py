employment = dict()
while True:
    line = input()
    if line == 'End':
        break

    company, id_number = line.split(' -> ')

    if company in employment.keys():
        if id_number not in employment[company]:
            employment[company].append(id_number)
    else:
        employment[company] = list()
        employment[company].append(id_number)

for key,value in employment.items():
    print(key)
    for num in employment[key]:
        print(f'-- {num}')