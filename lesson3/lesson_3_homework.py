# Task1
# def division(*numbers):
#     try:
#         number_1 = int(input("Введите делимое: "))
#         number_2 = int(input("Введите делитель: "))
#         result = number_1 / number_2
#     except ValueError:
#         return "Введены некорректные данные"
#     except ZeroDivisionError:
#         return "Делить на ноль - нельзя"
#     return result
# print(f"Результат: {division()}")


# Task2
# def user_data(last_name, first_name, year_birth, city, email, phone):
#     print(f"{last_name} {first_name}, {year_birth}, {city}, {email}, {phone}")
#
# user_data(last_name='Иван', first_name='Иванов', year_birth='1988', city='Москва', email='ivan@yandex.ru', phone=79001005050)


# Task3
# def my_func(var_1, var_2, var_3):
#     if var_1 > var_3 and var_2> var_3:
#         return var_1 + var_2
#     elif var_1 > var_2 and var_3 > var_2:
#         return var_1 + var_3
#     else: return var_2 + var_3
#
# print(my_func(80, 21, 20))


# Task4
# def my_func(x, y):
#     return x ** y
# print(f"Результат: {my_func(2, -2)}")


# # Task6
# def int_func(*args):
#     word = input("Введите слово с маленькой буквы: ")
#     print(word.title())
#     return
# int_func()
