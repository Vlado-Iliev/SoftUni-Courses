def func(ch1,ch2):
    for ch in range(ord(ch1 ) + 1, ord(ch2)):
        print(chr(ch),end=' ')



ch1 = input()
ch2 = input()
func(ch1,ch2)
