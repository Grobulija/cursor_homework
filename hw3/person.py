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
    def __init__(self, name, age, money_avail, homes_list=None):
        if homes_list is None:
            homes_list = []
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
        if random.randrange(0, 100) <= 3:
            print(f'Ooops! {self.name} slipped on a banana and broke his/her arm. \n'
                  f'All the money was spent on treatment and revenge on bananas. ')
        else:
            self.money_avail += salary
            print(f'{self.name} earn money. Total amount of money {self.money_avail}')

    def buy_house(self, house, realtor):
        if house not in realtor.houses_sale:
            print(f'There is no such house in the list!')
            return False
        if house.cost > self.money_avail:
            print(f'Person {self.name} does not have enough money')
            return False
        if realtor.steal_money():
            self.money_avail -= house.cost*0.3
            print(f'Realtor {realtor.name} steal money. Now {self.name} has {self.money_avail}')
            return False
        else:
            realtor.houses_sale.remove(house)
            self.pers_home.append(house)
            self.money_avail -= house.cost
            print(f' {self.name} bought house successfully with {house.cost}!')
            return True
