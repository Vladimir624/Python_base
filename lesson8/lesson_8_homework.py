# Чтобы снять комментирование с нескольких строк одновременно, выделите нужные строки и нажмите на Ctrl + /

# Task1

# class Date:
#     def __init__(self, day_month_year):
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def ext(cls, day_month_year):
#         my_date = []
#
#         for i in day_month_year.split():
#             if i != '-':
#                 my_date.append(i)
#
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#     @staticmethod
#     def valid(day, month, year):
#
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2000 <= year <= 2021:
#                     return f'OK'
#                 else:
#                     return f'Год должен быть указан от 2000 до 2021'
#             else:
#                 return f'Некоррекно указан месяц'
#         else:
#             return f'Некоррекно указан день'
#
#     def __str__(self):
#         return f'Числа даты {Date.ext(self.day_month_year)}'
#
# today = Date('11 - 1 - 2001')
# print(today)
# print(Date.valid(11, 11, 2001))


# Task2
# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# try:
#     number_1 = int(input("Введите делимое: "))
#     number_2 = int(input("Введите делитель: "))
#     result = number_1 / number_2
# except ZeroDivisionError:
#     print("Делить на ноль нельзя")
# else:
#     print(f"Результат: {result}")

# Task 4-6
# class Storehouse:
#     sku: int
#     name: str
#     quantity: int
#
#     def __init__(self, sku, name, quantity):
#         self.sku = sku
#         self.name = name
#         self.quantity = quantity
#         self.my_store = []
#         self.my_unit = {'SKU': self.sku, 'Модель устройства': self.name, 'Количество': self.quantity}
#
#     def __str__(self):
#         return f'sku {self.sku}, наименование {self.name}, количество: {self.quantity}'
#
#
#     def reception(self):
#         while True:
#             try:
#                 unit_sku = int(input(f'Введите SKU: '))
#                 unit_name = input(f'Введите наименование: ')
#                 unit_q = int(input(f'Введите количество: '))
#                 unique = {'SKU': unit_sku, 'Модель устройства': unit_name, 'Количество': unit_q}
#                 self.my_unit.update(unique)
#                 self.my_store.append(self.my_unit)
#                 print(f'Результат ввода {self.my_store}')
#             except:
#                 return f'Ошибка ввода данных'
#             else:
#                 exit('Ввод завершен')
#
# class Printer (Storehouse):
#     def to_print(self):
#         return f'print {self.quantity} times'
#
# class Scanner (Storehouse):
#     def to_scan(self):
#         return f'scan {self.quantity} times'
#
# class Xerox (Storehouse):
#     def to_xerox(self):
#         return f'xerox {self.quantity} times'
#
# unit_1 = Printer(55551, 'Принтер HP DSG-2341', 10)
# unit_2 = Scanner(56870, 'Сканер Canon F25BNS', 10)
# unit_3 = Xerox(66547, 'Xerox DDR-083765', 8)
# print(unit_1.reception())
# print(unit_2.reception())
# print(unit_3.reception())

