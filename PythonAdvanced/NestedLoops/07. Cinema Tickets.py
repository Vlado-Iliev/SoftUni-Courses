movie_name = input()
student_counter = 0
standard_counter = 0
kid_counter = 0
while movie_name != 'Finish':

    seats_taken = 0
    seats_finish = False

    free_seats = int(input())
    command = input()
    while command != 'End' and not seats_finish:
        if command == 'student':
            student_counter += 1
            seats_taken +=1
        elif command == 'standard':
            standard_counter += 1
            seats_taken += 1
        elif command == 'kid':
            kid_counter += 1
            seats_taken += 1
        percentage = seats_taken / free_seats * 100
        if percentage >= 100:
            seats_finish = True
        else:
            command = input()
    if command == 'End' or seats_finish:
        print(f'{movie_name} - {percentage:.2f}% full.')
        seats_finish = False
        movie_name = input()

total_tickets = kid_counter + student_counter + standard_counter
student_percent = student_counter / total_tickets * 100
standard_percent = standard_counter / total_tickets * 100
kid_percent = kid_counter / total_tickets * 100

print(f'Total tickets: {total_tickets}')
print(f'{student_percent:.2f}% student tickets.')
print(f'{standard_percent:.2f}% standard tickets.')
print(f'{kid_percent:.2f}% kids tickets.')