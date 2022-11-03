# Языки
# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.
# Входные данные
# Первая строка входных данных содержит количество школьников N.
# Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
# содержащих названия языков, которые знает i-й школьник.
# Пример входных данных:
# 	3          # N количество школьников
# 2          # M1 количество языков первого школьника
# Russian    # языки первого школьника
# English
# 3          # M2 количество языков второго школьника
# Russian
# Belarusian
# English
# 3
# Russian
# Italian
# French

n = int(input())
lang = []
for i in range(n):
    b = int(input())
    c = set()
    for j in range(b):
        c.add(input())
        lang.append(c)
unic = set.union(*lang)
intersec = set.intersection(*lang)
print(len(intersec), '\n'.join(sorted(intersec)), len(unic), '\n'.join(sorted(unic)), sep='\n')