def grade_mark(grade):
    if grade < 3:
        print('Fail')
    elif grade < 3.5:
        print('Poor')
    elif grade < 4.5:
        print('Good')
    elif grade < 5.5:
        print('Very Good')
    else:
        print('Excellent')


grade = float(input())
grade_mark(grade)