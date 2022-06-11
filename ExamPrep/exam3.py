data = dict()
line = input()
disliked_meals = 0
while line != 'Stop':
    line = line.split('-')
    guest = line[1]
    meal = line[2]
    if line[0] == 'Like':
        if guest in data:
            if meal in data[guest]:
                pass
            else:
                data[guest].append(meal)
        else:
            data[guest] = list()
            data[guest].append(meal)

    elif line[0] == 'Dislike':
        if guest not in data:
            print(f"{guest} is not at the party.")
        elif meal not in data[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            disliked_meals += 1
            print(f"{guest} doesn't like the {meal}.")
            data[guest].remove(meal)

    line = input()


for key,value in data.items():
    meals =', '.join(value)
    print(f'{key}: {meals}')

print(f'Unliked meals: {disliked_meals}')