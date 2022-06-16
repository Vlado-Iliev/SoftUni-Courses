stack = []
number = int(input())

for _ in range(number):
    command = input()
    if command.startswith('1 '):
        num = command.split(' ')
        stack.append(int(num[1]))

    elif command == '2':
        if stack:
            stack.pop()
    elif command == '3':
        print(max(stack))
    elif command == '4':
        print(min(stack))

new_stack = []
for _ in range(len(stack)):
    new_stack.append(str(stack.pop()))

print(', '.join(new_stack))