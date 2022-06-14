total_days = int(input())
type_of_room = input()
feedback = input()
nigts = total_days - 1
cost_per_nigt = 0
discount = 0
discounted_total = 0
cost = 0
#;room for one person; – 18.00 лв за нощувка
if type_of_room == 'room for one person':
    cost_per_nigt = 18
    cost = cost_per_nigt * nigts
    if nigts < 10 :
        discount = 0
    elif 10<= nigts < 15:
        discount = 0
    elif 15 < nigts :
        discount = 0
#;apartment; – 25.00 лв за нощувка
elif type_of_room == 'apartment' :
    cost_per_nigt = 25
    cost = cost_per_nigt * nigts
    if nigts < 10 :
        discount = cost* 0.30
    elif 10<= nigts < 15:
        discount = cost * 0.35
    elif 15 < nigts :
        discount = cost * 0.50
#president apartment; – 35.00 лв за нощувка
elif type_of_room == 'president apartment' :
    cost_per_nigt = 35
    cost = cost_per_nigt * nigts
    if nigts < 10 :
        discount = cost * 0.10
    elif 10<= nigts < 15:
        discount = cost * 0.15
    elif 15 < nigts :
        discount = cost * 0.20

discounted_total = cost - discount


if feedback == 'positive':
    final_cost = discounted_total * 1.25
elif feedback == 'negative':
    final_cost = discounted_total *  0.9

print(f'{final_cost:.2f}')

