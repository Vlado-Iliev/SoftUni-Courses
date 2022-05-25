from math import floor

# Потребителят въвежда 3 числа, по едно на ред:
# ⦁	Доход в лева - реално число;
income = float(input())
# ⦁	Среден успех -  реално числсо;
avrg_grade = float(input())
# ⦁	Минимална работна заплата – реално число
min_wage = float(input())
soc_scholarship = 0
grade_scholarship = 0
# Изискване за социална стипендия - доход на член от семейството по-малък от минималната работна заплата и успех над 4.5.
if income < min_wage and avrg_grade > 4.5:
    # Размер на социалната стипендия - 35% от минималната работна заплата
    soc_scholarship = min_wage * 0.35

# Изискване за стипендия за отличен успех - успех над 5.5, включително.
if avrg_grade >= 5.5:
    # Размер на стипендията за отличен успех - успехът на ученика, умножен по коефициент 25.
    grade_scholarship = avrg_grade * 25
# Изход

if grade_scholarship and soc_scholarship > 0:
    if grade_scholarship >= soc_scholarship:
        print(f"You get a scholarship for excellent results {floor(grade_scholarship)} BGN")
    else:
        print(f"You get a Social scholarship {floor(soc_scholarship)} BGN")

elif grade_scholarship > 0:
    print(f"You get a scholarship for excellent results {floor(grade_scholarship)} BGN")
elif soc_scholarship > 0:
    print(f"You get a Social scholarship {floor(soc_scholarship)} BGN")
else:
    print("You cannot get a scholarship!")

# ⦁	Ако ученикът няма право да получава стипендия, се извежда:
# "You cannot get a scholarship!"
# ⦁	Ако ученикът има право да получава само социална стипендия:
# "You get a Social scholarship {стойност на стипендия} BGN"
# ⦁	Ако ученикът има право да получава само стипендия за отличен успех:
# "You get a scholarship for excellent results {стойност на стипендията} BGN"
# ⦁	Ако ученикът има право да получава и двата типа стипендии, ще получи по-голямата по сума, а ако са равни ще получи тази за отличен успех.
# Резултатът се закръгля до по-малкото цяло число.
