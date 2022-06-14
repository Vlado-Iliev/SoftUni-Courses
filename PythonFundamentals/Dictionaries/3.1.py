countries = input().split(', ')
capitals = input().split(', ')
task = dict(zip(countries,capitals))

for keys,values in task.items():
    print(f'{keys} -> {values}')