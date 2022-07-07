from json import loads


def get_all_products():
    with open('./products.txt', 'r') as products_file:
        return [loads(line.strip()) for line in products_file]
