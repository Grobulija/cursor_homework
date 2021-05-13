from abc import ABC, abstractmethod


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
