def precondition(func):  # декоратор, устанавливающий и проверяющий предусловие

    def wrapper():  # функция-обёртка
        global n
        n = int(input())
        global fact
        fact = 1
        while n > 1:  # предусловие
            func()  # выполняем функцию
        print(fact)
    return wrapper


@precondition  # функция-декоратор
def factorial():  #
    fact *= n
    n -= 1


factorial()