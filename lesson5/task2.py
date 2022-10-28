# Создайте декоратор, который хранит результаты вызовов
# функции (за все время вызовов, не только текущий запуск программы)

def dec(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper

@dec
def fun():
    print('hello word')

fun()
fun()
fun()
fun()

print(fun.count)

