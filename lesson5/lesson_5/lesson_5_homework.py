# Task1
# with open('fail.text', 'a') as my_file:
#     while True:
#         line = input("Введите текст для записи в файл: ")
#         my_file.write(line + '\n')
#         if not line:
#             break

# Task2
# def cnt_line():
#     with open('task_2.text') as file:
#         my_line = file.readlines()
#         for l in range(len(my_line)):
#             cnt_l = my_line[l].split()
#             print(f'Количество строк в файле {len(my_line)}. В {l + 1}-ой строке {len(cnt_l)} слов(а)')
# cnt_line()

# Task5
# def summary():
#     try:
#         with open('fail_2.txt', 'w+') as file:
#             line = input('Введите цифры через пробел: \n')
#             file.writelines(line)
#             my_numb = line.split()
#
#             print(sum(map(int, my_numb)))
#     except IOError:
#         print('Ошибка в файле')
#     except ValueError:
#         print('Неправильно набран номер. Ошибка ввода-вывода')
# summary()