donated = input().split(', ')
number_of_beggers = int(input())

donations_num = list(map(int,donated))
beggers_bank = list()
for n in range(number_of_beggers):
    beggers_bank.append(donations_num[n])
for donations in range(number_of_beggers,len(donated) + 1):
    for n in range(number_of_beggers):
        donations_num[donations]




