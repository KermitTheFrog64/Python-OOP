# ввод чисел и добавление в список
def _input_():
    x = []
    for s in input().split():
        x.append(float(s))
    # x = [float(s) for s in input().split()]
    return x


# преобразование списка
def _convert_(a):
    for i in range(len(a)):
        a[i] *= 0.13
    a.sort()
    # y = [i * 0.13 for i in a].sort()
    return a


# вывод списка
def _print_(b):
    for elem in b:
        print(round(elem, 2), end=' ')


# сохранение в файл
def _save_(c):
    f = open('text.txt', 'w')
    for index in c:
        f.write(str(index) + '\n')
    f.close()


# основная часть
k = _input_()
h = _convert_(k)
_print_(h)
print("Want to save your data to a file? (Y/N)")
choice = input()
if choice == 'Y' or 'y':
    _save_(h)
