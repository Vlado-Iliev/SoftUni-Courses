change = float(input())
change = int(change * 100)
total_coins = 0


total_coins += change // 200
change %=200
total_coins += change // 100
change %= 100
total_coins += change // 50
change %= 50
total_coins += change // 20
change %= 20
total_coins += change // 10
change %= 10
total_coins += change // 5
change %= 5
total_coins += change // 2
change %= 2
if change == 1 :
    total_coins += 1


print (total_coins)