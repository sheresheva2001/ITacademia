# Найти самое длинное слово в введенном
# предложении. Учтите что в предложении есть знаки
# препинания.
# Подсказки:
# my_string.split([chars]) возвращает список строк.
# len(list) - количество элементов в списке

import string

my_string=str(input('введите предложение:'))
list= my_string.translate(str.maketrans('','', string.punctuation))
print(max(list.split(), key=len))
