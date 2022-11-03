# Оглянемся назад. Числа
# Даны два натуральных числа. Вычислите их наибольший общий делитель
# при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)