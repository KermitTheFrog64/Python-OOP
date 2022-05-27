# на вход подаётся строка
s = input()  # считываем строку целиком функцией input

# метод строки split() возвращает список строк, которые получатся, если исходную строку разрезать на части по пробелам
a = s.split()
# преобразовываем элементы списка по одному в числа
for i in range(len(a)):
    a[i] = float(a[i])

# a = [float(s) for s in input().split()] - в одну строку

b = [i * 0.13 for i in a]  # умножаем каждый элемент списка на 0.13
b.sort()  # сортируем исходный список

# вывод элементов списка, округлённых до двух знаков после запятой
for elem in b:
    print(round(elem, 2), end=' ')

print("Want to save your data to a file? (Y/N)")
choice = input()
if choice == 'Y' or 'y':
    f = open('text.txt', 'w')  # открываем файл
    for index in b:
        f.write(str(index) + '\n')  # записываем в файл
    f.close()  # закрываем файл
