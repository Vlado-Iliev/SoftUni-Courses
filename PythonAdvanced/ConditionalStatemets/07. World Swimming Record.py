#Вход
from math import floor
#От конзолата се четат 3 реда:
world_record = float(input())
#⦁	Рекордът в секунди – реално число;
distance_m =  float(input())
#⦁	Разстоянието в метри – реално число;
time_for_one_meter_sec = float(input())
#	Времето в секунди, за което плува разстояние от 1 м. - реално число.
his_time = distance_m * time_for_one_meter_sec
added_distance = floor(distance_m / 15)
added_time = added_distance * 12.5

his_total_time = his_time + added_time
if his_total_time < world_record :
    print(f" Yes, he succeeded! The new world record is {his_total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(world_record - his_total_time):.2f} seconds slower.")
#Изход
#  Отпечатването на конзолата зависи от резултата:
#⦁	Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
#⦁	" Yes, he succeeded! The new world record is {времето на Иван} seconds."
#⦁	Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
#⦁	"No, he failed! He was {недостигащите секунди} seconds slower."
#Резултатът трябва да се форматира до втория знак след десетичната запетая.

