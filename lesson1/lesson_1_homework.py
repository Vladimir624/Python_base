# Task_1
a = 5
b = a + 2
print(b)
print(a+b)

rf = 'Москва -'
it = 'Рим'
print(rf,it)

# Task_2
time_s = int(input("Введите время в секундах: "))
m = (time_s // 60) % 60
h = (time_s // 3600) % 24
s = time_s % 60
print("Минуты:",m)
print("Часов:",h)
print("ЧЧ:ММ:СС:",'%d:%02d:%02d' % (h, m, s))

# Task_3
n = int(input('Введите число: '))
nn = n * 11
nnn = n * 111
sum = n + nn + nnn
print(n, '+', nn, '+',nnn, '=',sum)

# Task_4
number = int(input('Введите целое положительное число: '))
r = 0
while number > 10:
   d = number % 10
   number = number // 10
   if d > r:
       r = d
else:
    print(number)
