# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner. (все станет проще когда мы изучим модули,
# getattr и setattr)
# runner() – все фукнции вызываются по очереди
# runner(‘func_name’) – вызывается только функцию func_name.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции
def fun1():
    dict = {i: i**3 for i in range(1, 21)}
    print(dict)

def fun2():
    list_1 = [1, 2, 3, 1, 3, 4, 5, 6, 5, 7]
    list_2 = []

    for i in list_1:
        if list_1.count(i) == 1:
            list_2.append(i)
    print(list_2)

def fun3():
    list = [0, 1, 0, 3, 0, 2]

    for i in range(len(list)):
        if list[i] != 0:
            print(list[i], end=' ')
    for i in range(list.count(0)):
        print(0, end=' ')

def fun4():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 2, 9, 5]
    c = []
    for i in a:
        for j in b:
            if i == j:
                c.append(i)
    print(c)


def runner(*args):
    if len(args) == 0:
        fun1()
        fun2()
        fun3()
        fun4()
    else:
        for i in args:
            globals()[i]()

runner()
runner('fun3')
runner('fun2', 'fun4')
