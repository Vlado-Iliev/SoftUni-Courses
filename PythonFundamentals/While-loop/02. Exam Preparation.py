number_of_failed_exercise = int(input())

name_of_exercise = input()


exercise_counter = 0
grade_counter = 0
failed_exercise_counter = 0
last_exercise = str

while name_of_exercise != 'Enough':
    score_from_exercise = int(input())
    exercise_counter += 1
    grade_counter += score_from_exercise
    last_exercise = name_of_exercise
    if score_from_exercise <= 4:
        failed_exercise_counter += 1
        if failed_exercise_counter >= number_of_failed_exercise:
            break
    name_of_exercise = input()


average_grade = grade_counter / exercise_counter

if failed_exercise_counter >= number_of_failed_exercise:
    print(f'You need a break, {failed_exercise_counter} poor grades.')
else:
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {exercise_counter}')
    print(f'Last problem: {last_exercise}')
