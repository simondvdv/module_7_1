from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        products = open(self.__file_name, 'r')
        print(products.read())
        products.close()

    def add(self, *args):
        products = open(self.__file_name, 'a')
        products_r = open(self.__file_name, 'r')
        for i in args:
            print(i.name)
            print(i.name in products_r.read())
            if not (i.name in products_r.read()):
                products.write(f'{i.name}, {i.weight}, {i.category}\n')
        products.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)



