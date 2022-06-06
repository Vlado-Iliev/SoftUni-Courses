people = int(input())
train = input().split(' ')
train = list(map(int,train))
condition = True

for wagon in range(len(train)):
    while train[wagon] < 4:
        if people <= 0:
            break
        people -= 1
        train[wagon] += 1

if sum(train) >= len(train) * 4:
    condition = False

if people == 0 and not condition:
    print(' '.join(list(map(str, train))))

if people == 0 and condition:
    print('The lift has empty spots!')
    print(' '.join(list(map(str, train))))

if people > 0 and not condition:
    print(f"There isn't enough space! {people} people in a queue!")
    print(' '.join(list(map(str, train))))

