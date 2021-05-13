from house import House, SmallHouse
from person import Person
from realtor import Realtor


if __name__ == "__main__":
    mansion = House(78000.0, 120)
    cottage = House(19000.0, 33)
    forestHouse = SmallHouse(10000.0)
    mountHouse = SmallHouse(33000.0)
    lakeHouse = House(45600.0, 66)

    print('Input name, age and budget of person:')
    humanFirst = Person(input(), input(), float(input()), [lakeHouse])
    humanFirst.provide_inform()

    print('Input name of realtor and available discounts:')
    realtorFirst = Realtor(input(), float(input()), [mansion, mountHouse])
    realtorFirst.provide_info_all_houses()

    humanFirst.buy_house(mountHouse, realtorFirst)
    humanFirst.make_money(14450.0)
    realtorFirst.offer_discount(mountHouse)
    humanFirst.buy_house(mountHouse, realtorFirst)

    humanFirst.provide_inform()
    realtorFirst.provide_info_all_houses()
