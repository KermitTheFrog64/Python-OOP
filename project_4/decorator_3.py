def postcondition(func):  # декоратор, устанавливающий и проверяющий постусловие

    def wrapper():  # функция-обёртка
        a = 1
        b = 100
        x = a
        while True:
            func(x)  # выполняем функцию
            if x <= b:
                break
    return wrapper


@postcondition  # функция-декоратор
def iseven(i):
    if i % 2 == 0:
        print(i)
    i += 1


iseven()