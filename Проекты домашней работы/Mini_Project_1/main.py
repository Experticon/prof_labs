# Среда аренды транспорта
class Transport_Rent:

    # Отсюда транспортные средства будут получать основу стоимости топлива и транспорта
    def __init__(self):
        self.cost = 500
        self.fuel_consumption = 25

    # Вывод чека
    def make_bill(self, a, b):
        __c = self.__extra_paid_bank(a, b)
        print("///////////////////////////////////")
        print("          Стоимость аренды         ")
        print(a)
        print("     Стоимость топлива за путь     ")
        print(b)
        print("    Итого с учётом комиссии в 39%  ")
        print(a + b + __c)
        print("///////////////////////////////////")


    # Пользователю НЕ НУЖЕН доступ к вычислению банковской комиссии - ИНКАПСУЛЯЦИЯ
    def __extra_paid_bank(self, a, b):
        __c = (a + b) * 0.39
        return __c


# Эти классы наследуют основу стоимостей. Также можно воспользоваться НЕСКОЛЬКИМИ видами
# транспорта - НАСЛЕДОВАНИЕ И ИНКАПСУЛЯЦИЯ
class Auto(Transport_Rent):

    def getCost(self):
        return self.cost * 5

    def getConsumption(self):
        return self.fuel_consumption * 3


class Motorcycle(Transport_Rent):

    def getCost(self):
        return self.cost * 2

    def getConsumption(self):
        return self.fuel_consumption


class Truck(Transport_Rent):

    def getCost(self):
        return self.cost * 3

    def getConsumption(self):
        return self.fuel_consumption * 4


# Едиснтвенная команда, которой пользуется пользователь
def rent_ride(transport, km):

    transport_cost = transport.getCost()
    ride_cost = transport.getConsumption() * km
    Transport_Rent.make_bill(transport, transport_cost, ride_cost)


if __name__ == '__main__':

    my_auto = Auto()
    my_motorcycle = Motorcycle()
    my_truck = Truck()

    rent_ride(my_auto, 50)
    rent_ride(my_motorcycle, 120)
    rent_ride(my_truck, 300)
