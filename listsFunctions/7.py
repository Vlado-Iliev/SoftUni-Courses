def age_distributor(list_of_guests):
    current_age_group = 10
    while len(list_of_guests) > 0:
        current_group = [g for g in list_of_guests if g <= current_age_group]
        print(f"Group of {current_age_group}'s: {current_group}")
        for person in current_group:
            if int(person) in list_of_guests:
                list_of_guests.remove(int(person))
        current_age_group += 10


guests = input().split(', ')
guest_list = list(map(int,guests))
age_distributor(guest_list)
