import csv


class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name:str, price:int, quantity:int=0):
        #Check if attributes are in range
        assert price >= 0
        assert quantity >= 0

        #Assign values as expected
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #Execute some final actions
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Value of name cannot be more than 10 characters")
        else:
            self.__name = value

    def calculate_total_costs(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price *= self.pay_rate

    #Decorator to convert this into a class method
    @classmethod
    def instantiate_from_csv(cls, filename):
        with open (filename, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item (
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_a_decimal(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"