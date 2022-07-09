def sorted_result(fridge):
    condition = True
    result_string = f''
    for key in fridge.keys():
        if len(fridge[key]) != 0:
            condition = False
    if condition:
        return 'No products in the cart!'

    result = {k:[v for v in sorted(fridge[k],)] for k in sorted(fridge, key=lambda k: (-len(fridge[k]),k[1]))}
    for key,value in result.items():
        result_string += f'{key}:\n'
        if len(value) > 0:
            for product in value:
                result_string += f' - {product}\n'
    return result_string.strip()


def shopping_cart(*args):
    fridge = {'Pizza': [],'Soup':[],'Dessert':[]}
    for product in args:
        if product == 'Stop':
            return sorted_result(fridge)
            
        meal,ingrediance = [x for x in product]

        if ingrediance in fridge[meal]:
            continue
        else:
            if meal == 'Pizza' and len(fridge[meal]) < 4:
                fridge[meal].append(ingrediance)
            elif meal == 'Soup' and len(fridge[meal]) < 3:
                fridge[meal].append(ingrediance)
            elif meal == 'Dessert' and len(fridge[meal]) < 2:
                fridge[meal].append(ingrediance)

    return sorted_result(fridge)


