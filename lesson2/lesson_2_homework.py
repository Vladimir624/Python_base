# Task_1
# simple_list = [55, 'Задание № 1', 44.5, None]
# print(simple_list)
#
# for simple in simple_list:
#     print (f"{simple} == {type (simple)}")


# Task_2
# super_list = ['11', '22', '33', '44', '55']
# if len(super_list) % 2 == 0:
#     i = 0
#     while i < len(super_list):
#         el = super_list[i]
#         super_list[i] = super_list[i+1]
#         super_list[i+1] = el
#         i += 2
# else:
#     i = 0
#     while i < len(super_list) - 1:
#         el = super_list[i]
#         super_list[i] = super_list[i + 1]
#         super_list[i + 1] = el
#         i += 2
# print(super_list)


# Task_3
# number = int(input('Введите номер месяца >>> ' ))
# if number >=1 and number <=12:
#     months = {1: "Зима",
#               2: "Зима",
#               3: "Весна",
#               4: "Весна",
#               5: "Весна",
#               6: "Лето",
#               7: "Лето",
#               8: "Лето",
#               9: "Осень",
#               10: "Осень",
#               11: "Осень",
#               12: "Зима"
#               }
#     print(months.get(number))
# else: print('Вводимое число должно быть от 1 до 12')


# Task_4
# my_str = input("Введите слова >>> ")
# a = my_str.split(' ')
# for ind, el in enumerate(a, 1):
#     if len(el) > 10:
#         el = el[0:10]
#     print(f"{ind}) - {el}")