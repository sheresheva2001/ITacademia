# Написать программу которая находит ближайшую степень двойки к
# введенному числу. 10(8), 20(16), 1(1), 13(16)


def nearest_degree(n):
    res = 0
    for i in range(n, 0, -1):
        if ((i & (i - 1)) == 0):
            res = i
            break
    return res

n = 13
print(nearest_degree(n))

