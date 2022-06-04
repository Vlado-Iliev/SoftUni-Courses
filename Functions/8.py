def palindrome_check(list):
    for numbers in list:
        if numbers == numbers[::-1]:
            print('True')
        else:
            print('False')


palindrome_check(input().split(", "))