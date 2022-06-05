order = input().split(' ')
palindrome = list(filter(lambda x: x == x[::-1],order))
chosen = input()

print(palindrome)
print(f'Found palindrome {palindrome.count(chosen)} times')
