from collections import deque

box = deque(input().split(' '))
box = deque(map(int,box))

hanger_capacity = int(input())
hanger_counter = 1
current_hanger = 0
for _ in range(len(box)):
    piece_of_clothing = box.pop()
    if current_hanger + piece_of_clothing <= hanger_capacity:
        current_hanger += piece_of_clothing
    else:
        hanger_counter += 1
        current_hanger = piece_of_clothing

print(hanger_counter)

