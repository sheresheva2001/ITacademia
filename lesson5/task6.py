# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4)

# Проверить, является ли заданное натуральное число степенью двойки

num = int(input('введите число:'))
max_divider = 1
for i in range(num-1, 1, -1):
    if (num % 1 == 0):
        if (max_divider < i):
            max_divider = i

b = 0

while max_divider != 1:
    if max_divider % 2 !=0:
        break
    b += 1

print('максимальный делитель:', b)
