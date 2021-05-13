

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.__class__.__name__} {self.name} is eating.')

    def sleep(self):
        print(f'{self.__class__.__name__} {self.name} is sleeping.')


class Koala(Animal):
    def climb(self):
        print(f'{self.__class__.__name__} {self.name} is climbing the eucalyptus.')


class Fox(Animal):
    def sniff(self):
        print(f'{self.__class__.__name__} {self.name} is sniffing.')

    def sneak(self):
        print(f'{self.__class__.__name__} {self.name} is sneaking.')


class BlueWren(Animal):
    def fly(self):
        print(f'{self.__class__.__name__} {self.name} is flying.')


class Giraffe(Animal):
    def run(self):
        print(f'{self.__class__.__name__} {self.name} is running like in slow motion.')


class HumpbackWhale(Animal):
    def swim(self):
        print(f'{self.__class__.__name__} {self.name} is swimming.')

    def sing(self):
        print(f'{self.__class__.__name__} {self.name} is singing.')


class Human:
    def __int__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.__class__.__name__} {self.name} is eating.')

    def sleep(self):
        print(f'{self.__class__.__name__} {self.name} is sleeping.')

    def study(self):
        print(f'{self.__class__.__name__} {self.name} is studying.')

    def work(self):
        print(f'{self.__class__.__name__} {self.name} is working.')


class Centaur(Human, Animal):
    def stargazing(self):
        print(f'{self.__class__.__name__} {self.name} is stargazing at night.')

    def plant(self):
        print(f'{self.__class__.__name__} {self.name} is planting moon flowers.')


if __name__ == "main":
    koala = Koala('Buster Moon')
    fox = Fox('Nick Wild')
    blueWren = BlueWren('Fred')
    giraffe = Giraffe('Melman')
    humpbackWhale = HumpbackWhale('Destiny')

    print(f'/#1:/')
    koala.climb()
    fox.sniff()
    fox.sneak()
    blueWren.fly()
    giraffe.run()
    humpbackWhale.swim()
    humpbackWhale.sing()

    print(f'koala: {isinstance(koala, Animal)}')
    print(f'fox: {isinstance(fox, Animal)}')
    print(f'blue wren: {isinstance(blueWren, Animal)}')
    print(f'giraffe: {isinstance(giraffe, Animal)}')
    print(f'humpback whale: {isinstance(humpbackWhale, Animal)}')

    print(f'/#1.a:/')
    centaur = Centaur("Oreius")
    centaur.eat()
    centaur.sleep()
    centaur.study()
    centaur.work()
    centaur.stargazing()
    centaur.plant()