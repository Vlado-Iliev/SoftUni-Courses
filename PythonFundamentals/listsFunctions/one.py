word = input()
vowels = ['a', 'o', 'u', 'e', 'i']
new_word = [ch for ch in word if ch not in vowels]

print(''.join(new_word))