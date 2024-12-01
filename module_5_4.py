class House:

    house_history = []

    def __new__(cls, *args, **kwargs):
        cls.house_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors): #house_history):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(0, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
        else:
            print('Такого этажа не существует')

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')

h1 = House('Хрущёвка', 5)
print(House.house_history)
h2 = House('ЖК Лучшая жизнь', 25)
print(House.house_history)
h3 = House('ЖК Дубный', 30)
print(House.house_history)
del h2
del h3
print(House.house_history)