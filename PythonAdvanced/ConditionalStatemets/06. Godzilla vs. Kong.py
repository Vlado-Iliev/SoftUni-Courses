# вход
film_budget = float(input())
number_statists = int(input())
price_for_clothes_for_one_statist = float(input())

cost_for_clothes = 0
total_price = 0
#   ⦁	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
if 1.00 <= film_budget <= 1000000.00 :

#   ⦁	Брой на статистите – цяло число в интервала [1 … 500]
    if 1<= number_statists <= 500 :

#   ⦁	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
        if 1.00 <= price_for_clothes_for_one_statist <= 1000.00:
# пресмятане
            cost_for_clothes = number_statists * price_for_clothes_for_one_statist
            #   ⦁	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
            if number_statists > 150 :
                cost_for_clothes *= 0.90

# пресмятане
#   ⦁	Декорът за филма е на стойност 10% от бюджета.
            decours = film_budget * 0.10
            total_price = decours + cost_for_clothes
# изход
if total_price <= film_budget :
    print ("Action!")
    print (f"Wingard starts filming with {(film_budget - total_price):.2f} leva left.")
else:
    print ("Not enough money!")
    print(f"Wingard needs {abs(film_budget-total_price):.2f} leva more.")

#  На конзолата трябва да се отпечатат два реда:
#   ⦁	Ако  парите за декора и дрехите са повече от бюджета:
#   ⦁	"Not enough money!"
#   ⦁	"Wingard needs {парите недостигащи за филма} leva more."
#   ⦁	Ако парите за декора и дрехите са по малко или равни на бюджета:
#   ⦁	"Action!"
#   ⦁	"Wingard starts filming with {останалите пари} leva left."
#   Резултатът трябва да е форматиран до втория знак след десетичната запетая.