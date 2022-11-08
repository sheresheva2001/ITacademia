# Создайте декоратор, который хранит результаты вызовов
# функции (за все время вызовов, не только текущий запуск программы)

prev_result = None

def remember(func):

    def wrapper(*args):
        global prev_result
        print(f"Prev result = '{prev_result}'")
        prev_result = func(*args)
    return wrapper

@remember
def summarize(*args):
    result = ""
    for i in args:
        result += i
    print('New result = ', result)
    return result

summarize('cat')
summarize('world')
summarize('hello')
summarize('good')


