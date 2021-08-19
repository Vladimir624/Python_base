# Task_1
# def salary_bonus(hours, rate, bonus):
#     hours = int(input("Введите количество отработанных часов за месяц: "))
#     rate = int(input("Введите ставку часа: "))
#     bonus = float(input("Введите процент премии, как десятичная дробь: "))
#     salary = (hours * rate)
#     return (salary * bonus) + salary
#
# print(f"Месячная зарплата с учетом премии: {salary_bonus(40, 1000, 0.1)} рублей")


# Task_2
# import random
#
# numbers_list = [x for x in range(5, 100, 15)]
# random.shuffle(numbers_list)
# print(numbers_list)
#
# processed_numbers_list = []
# for el in range(len(numbers_list) - 1):
#     if numbers_list[el] < numbers_list[el+1]:
#         processed_numbers_list.append(numbers_list[el+1])
# print(processed_numbers_list)


# Task_3
# numbers_list = [x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0]
# print(numbers_list)


# Task_4
# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#
# uniq = [x for x in my_list if my_list.count(x) == 1]
# print(uniq)


# Task_5
# from functools import reduce
#
# def my_func (x1, x2):
#     return x1 + x2
#
# lst = [x for x in range(100, 1001, 300)]
# print(lst)
#
# lst2 = reduce(my_func, lst)
# print(lst2)


# Task_6a
# from itertools import count
# for el in count(3):
#     if el >10:
#         break
#     else:
#         print(el)

# Task_6b
# from itertools import cycle
# lst_1 = list(range(4))
# print(lst_1)
#
# for x, y in enumerate(cycle(lst_1 )):
#     print(y, end=" ")
#     if x >10:
#         print()
#         break