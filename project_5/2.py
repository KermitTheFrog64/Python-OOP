class Found(Exception):
    pass


def check():
    string = input("Введите число: ")
    if string.isnumeric():
        number = int(string)
        print(number)
        raise Found()
    else:
         return


try:
    check()
except Found:  # Исключение, если элемент - число
    print('The element is a number!')
else:  # иначе: элемент не число
    print('The element is not number!')
