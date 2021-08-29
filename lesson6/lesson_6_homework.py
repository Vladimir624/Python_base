# Чтобы снять комментирование с нескольких строк одновременно, выделите нужные строки и нажмите на Ctrl + /

# Task1
# from time import sleep
#
# class TrafficLight:
#     __color: str
#
#     def running (self):
#         i = 0
#
#         while i != 3:
#             self.__color = 'КРАСНЫЙ'
#             if i == 0:
#                 print(f'Горит {self.__color} цвет!')
#                 sleep(7)
#
#             self.__color = 'ЖЁЛТЫЙ'
#             if i == 1:
#                 print(f'Горит {self.__color} цвет!')
#                 sleep(2)
#
#             self.__color = 'ЗЕЛЁНЫЙ'
#             if i == 2:
#                 print(f'Горит {self.__color} цвет!')
#                 sleep(5)
#             i += 1
#
# traffic_light = TrafficLight()
# print(traffic_light.running())

# Task2
# class Road:
#     __length: int
#     __width: int
#     mass: int
#     thick: int
#
#     def __init__(self, mass, thick):
#         self.__length = 20
#         self.__width = 5000
#         self.mass = mass
#         self.thick = thick
#
#     def asphalt(self):
#         result = self.__length * self.__width * self.mass * self.thick / 1000
#         print(f'Покрытие всего дорожного полотна составит: {result} т')
#
# lokation1 = Road(25, 5)
# lokation1.asphalt()

# Task3
from typing import Iterable

# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": int(wage), "bonus": int(bonus)}
#
#
# class Position(Worker):
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         return self.name + " " + self.surname + ":"
#
#     def get_total_income(self):
#         return self._income["wage"] + self._income["bonus"]
#
# worker_1 = Position("Иван", "Петров", "Driver", 10000, 2000)
# print(worker_1.get_full_name(), worker_1.get_total_income())


# Task6
# class Stationery:
#     title: str
#
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return print("Запуск отрисовки")
#
# class Pen(Stationery):
#     def draw(self):
#         return print(f"Запуск отрисовки {self.title}")
#
# class Pencil(Stationery):
#     def draw(self):
#         return print(f"Запуск отрисовки {self.title}")
#
# class Handle(Stationery):
#     def draw(self):
#         return print(f"Запуск отрисовки {self.title}")
#
# pen = Pen("ручкой")
# pen.draw()
#
# pencil = Pencil("карандашём")
# pen.draw()
#
# handle = Handle("маркером")
# pen.draw()


