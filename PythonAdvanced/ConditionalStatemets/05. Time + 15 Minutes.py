#вход :
# час и минути
hours = int(input())
minutes = int(input())

#добавяне на 15 мин
minutes += 15
# форматиране на минути и часове (60 / 23)
if minutes > 59 :
    hours += (minutes // 60)
    minutes %= 60
if hours > 23 :
    hours %= 24


#форматиране на изход в 00 : 00 формат

if minutes >= 10:
     print (f"{ hours }:{minutes} ")
else :
     print (f"{ hours }:0{minutes} ")
