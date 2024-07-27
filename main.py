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
        product_string = products.read()
        answer = ''
        product_list = product_string.replace('\n', ', ').replace(' ', '').split(',')
        for i in range(0, len(product_list), 3):
            answer += product_list[i] + ' '
        return answer


    def add(self, *args):
        for i in args:
            products = open(self.__file_name, 'a')
            if not (i.name in Shop.get_products(self)):
                products.write(f'{i.name}, {i.weight}, {i.category}\n')
            else:
                print(f'Товар {i.name} уже есть в магазине')
            products.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())


