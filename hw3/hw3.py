from abc import ABC, abstractmethod
import random


class Human(ABC):
    @abstractmethod
    def provide_inform(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, *args, **kwargs):
        raise NotImplementedError


class Person(Human):
    def __init__(self, name, age, money_avail, homes_list=[]):
        self.name = name
        self.age = age
        self.money_avail = money_avail
        self.pers_home = homes_list

    def provide_inform(self):
        print(f'\nInformation about person:\n'
              f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Available money: {self.money_avail}\n'
              f'Person`s property:')
        for house in self.pers_home:
            print(f'{self.pers_home.index(house)}: {str(house)}')

    def make_money(self, salary: (int, float)):
        # Це було необов'язково, але дуже кортіло
        if random.randrange(0, 100) <= 3:
            print(f'Ooops! {self.name} slipped on a banana and broke his/her arm. \n'
                  f'All the money was spent on treatment and revenge on bananas. ')
        else:
            self.money_avail += salary
            print(f'{self.name} earn money. Total amount of money {self.money_avail}')

    def buy_house(self, house, realtor):
        if house not in realtor.houses_sale:
            print(f'There is no such house in the list!')
            return
        if house.cost > self.money_avail:
            print(f'Person {self.name} does not have enough money')
            return
        if realtor.steal_money():
            self.money_avail -= house.cost*0.3
            print(f'Realtor {realtor.name} steal money. Now {self.name} has {self.money_avail}')
        else:
            realtor.houses_sale.remove(house)
            self.pers_home.append(house)
            self.money_avail -= house.cost
            print(f' {self.name} bought house successfully with {house.cost}!')


class Home(ABC):
    @abstractmethod
    def apply_discount(self, *args, **kwargs):
        raise NotImplementedError


class House(Home):
    def __init__(self, cost, area):
        self.cost = cost
        self.area = area

    def apply_discount(self, discount):
        self.cost *= 1 - discount / 100

    def __str__(self):
        return f'House cost: {self.cost}, area {self.area}m^2'


class SmallHouse(House):
    def __init__(self, cost, area=40):
        super().__init__(cost, area)


class RealtorCity(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorCity):
    def __init__(self, name, discount, houses_sale=[]):
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
        else:
            print(f'Yay! Realtor {self.name} can offer a {self.discount}% off.')
            house.apply_discount(self.discount)
            print(f'Price after discount applied: {house.cost}.')

    def steal_money(self):
        rnd = random.randrange(0, 100)
        if rnd <= 10:
            return True
        else:
            return False


if __name__ == "__main__":
    mansion = House(78000.0, 120)
    cottage = House(19000.0, 33)
    forestHouse = SmallHouse(10000.0)
    mountyHouse = SmallHouse(33000.0)
    lakeHouse = House(45600.0, 66)

    print('Input name, age and budget of person:')
    humanFirst = Person(input(), input(), float(input()), [lakeHouse])
    humanFirst.provide_inform()

    print('Input name of realtor and available discounts:')
    realtorFirst = Realtor(input(), float(input()), [mansion, mountyHouse])
    realtorFirst.provide_info_all_houses()

    humanFirst.buy_house(mountyHouse, realtorFirst)
    humanFirst.make_money(14450.0)
    realtorFirst.offer_discount(mountyHouse)
    humanFirst.buy_house(mountyHouse, realtorFirst)

    humanFirst.provide_inform()
    realtorFirst.provide_info_all_houses()
