class Catalogue:
    def __init__(self,name: str):
        self.name = name
        self.products = list()

    def add_product(self,product_name: str):
        self.products.append(product_name)
    def get_by_letter(self,first_letter: str):
        current_list = list()
        for product in self.products:
            if product[0] == first_letter:
                current_list.append(product)
        return current_list
    def __repr__(self):
        return f'Items in the {self.name} catalogue:'
        self.products.sort()
        for product in self.products:
            return product






catalogue = Catalogue('Furniture')
catalogue.add_product('Sofa')
catalogue.add_product('Mirror')
catalogue.add_product('Desk')
catalogue.add_product('Chair')
catalogue.add_product('Carpet')
print(catalogue.get_by_letter('C'))
print(catalogue)