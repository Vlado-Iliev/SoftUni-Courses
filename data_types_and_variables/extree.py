number_of_people = int(input())
cappacity = int(input())
count = 0

while number_of_people > 0:
    count += 1
    number_of_people -= cappacity

print(count)
