#!env/bin/python3
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        print(f'Point x: {self.x} Point y: {self.y}')

    def __repr__(self):
        return f'Point x: {self.x} Point y: {self.y}'

class Product:
    def __init__(self, name, price, discount=0, stock=0, max_discount=20.0):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Название товара должно быть длиннее 2 символов')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.max_discount = abs(int(max_discount))
        if self.max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        self.discount = abs(float(discount))
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        self.stock -= items_count

    def discounted(self):
        return self.price - (self.price * self.discount / 100)

    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price},stock: {self.stock}>'


def main():
    my_point = Point(1, 2)
    my_point.coordinates()
    my_point.x = 100
    my_point.coordinates()
    print(my_point)

    my_phone = Product('iPhone 12', 100, stock=5)
    print(my_phone)
    my_phone.sell(2)
    print(my_phone)

    my_phone2 = Product('iPhone 11', 80, stock=50)
    print(my_phone2)
    my_phone2.sell(10)
    print(my_phone2)

if __name__ == "__main__":
    main()
