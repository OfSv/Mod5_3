# Перегрузка операторов
# Задача "Нужно больше этажей"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to_(self, new_floor):
        if type(new_floor) != int or new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i+1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return "Название: " + self.name + ", кол-во этажей: " + str(self.number_of_floors)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


House_1 = House('ЖК Эльбрус', 10)
House_2 = House('ЖК Лесное', 20)

print(House_1)
print(House_2)

print(House_1 == House_2)  # __eq__

House_1 = House_1 + 10  # __add__
print(House_1)

print(House_1 == House_2)

House_1 += 10  # __iadd__
print(House_1)

House_2 = 10 + House_2  # __radd__
print(House_2)

print(House_1 > House_2)  # __gt__
print(House_1 >= House_2)  # __ge__
print(House_1 < House_2)  # __lt__
print(House_1 <= House_2)  # __le__
print(House_1 != House_2)  # __ne__
