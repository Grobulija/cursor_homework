import random


class RealtorCity(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorCity):
    def __init__(self, name, discount, houses_sale=None):
        if houses_sale is None:
            houses_sale = []
        self.name = name
        self.discount = discount
        self.houses_sale = houses_sale

    def provide_info_all_houses(self):
        print(f'\nRealtor {self.name} sells only this houses:')
        for house in self.houses_sale:
            print(f'{self.houses_sale.index(house)}: {str(house)}')

    def offer_discount(self, house):
        if house not in self.houses_sale:
            print(f'This house is not on the list.')
            return False
        else:
            print(f'Yay! Realtor {self.name} can offer a {self.discount}% off.')
            house.apply_discount(self.discount)
            print(f'Price after discount applied: {house.cost}.')
            return True

    @staticmethod
    def steal_money():
        return random.randrange(0, 100) <= 10
