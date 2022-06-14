snowballs = int(input())
best_value = 0
text = ''
for _ in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight/time) ** quality
    if value > best_value:
        best_value = value
        text = f'{weight} : {time} = {int(value)} ({quality})'

print(text)