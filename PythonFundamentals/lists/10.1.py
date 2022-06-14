def second_chance(data):
    current_max_num = 0
    special = ''
    for ch in data:
        if current_max_num >= 6:
            break
        if ch != special:
            special = ch
            current_max_num = 1
        else:
            current_max_num += 1

    return special, current_max_num


def ticket_validator(data):
    special_char = '@#$^'
    for ticket in data:
        ticket = ticket.strip()
        if len(ticket) == 20:
            if ticket == ticket[0] * 20 and ticket[0] in special_char:
                print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
            else:
                tick1 = ticket[0:10]
                tick2 = ticket[11:20]
                if second_chance(tick1) > second_chance(tick2):
                    data_source = second_chance(tick2)
                else:
                    data_source = second_chance(tick1)

                if data_source[0] in special_char and data_source[1] >= 6:
                    print(f'ticket "{ticket}" - {data_source[1]}{data_source[0]}')
                else:
                    print(f'ticket "{ticket}" - no match')

        else:
            print('invalid ticket')


line = input().split(', ')
ticket_validator(line)