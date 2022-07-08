def naughty_or_nice_list(*args,**kwargs):
    result = {'Nice': [],'Naughty': [], 'Not Found': []}
    result_string = f''
    santa_list = args[0]
    santa = {x[0] : x[1] for x in santa_list}
    print(santa)
    first_commands = args[1:]
    second_commands = kwargs
    for c in first_commands:
        command = c.split('-')
        counter = 0
        for key in santa.keys():
            if key == command[0]:
                counter += 1
        if counter > 1:
            continue
        elif counter == 1:
            result[command[0]].append(santa[command[1]])
        elif counter == 0:
            result['Not Found'].append(santa[command[1]])

    for key,value in second_commands.items():
        for children in santa.keys():
            if key == children:
                result[value].append(key)

    for key,value in result:
        result_string += f'{key}: {", ".join([x for x in value])}'
    return result_string





print(naughty_or_nice_list( 
    [ (3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
