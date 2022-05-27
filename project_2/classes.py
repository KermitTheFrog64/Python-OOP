from statistics import mean


class Person:
    # конструктор
    def __init__(self, name, uni="ITMO"):
        self.__name = name  # устанавливаем имя
        self.__age = 18  # устанавливаем возраст
        self.uni = uni  # устанавливаем место работы/учёбы

    # сеттер
    def set_age(self, age):
        if age in range(1, 100):  # можно изменить возраст в зависимости от условия
            self.__age = age
        else:
            print("Недопустимый возраст")

    # геттер
    def get_age(self):
        return self.__age  # получаем возраст

    # геттер
    def get_name(self):
        return self.__name  # получаем имя

    # вывод информации на экран
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age, "\tУниверститет:", self.uni)

    # перегрузка оператора сравнения
    def __eq__(self, other):
        return self.__name == other.__name and self.__age == other.__age


class Teacher(Person):

    # переопределяем конструктор базового класса
    def __init__(self, name, work_experience, faculty, work_hours, uni="ITMO"):
        Person.__init__(self, name, uni="ITMO")
        self.experience = work_experience  # устанавливаем стаж
        self.faculty = faculty  # устанавливаем факультет
        self.work_hours = work_hours  # устанавливаем рабочие часы
        self.address = None

    # вывод дополнительной информации на экран
    def display_info(self):
        Person.display_info(self)
        print("Стаж:", self.experience, "\tФакультет:", self.faculty, "\tРабочие часы в текущем году:", self.work_hours)

    # расчёт премии
    def premium(self):
        if self.work_hours in range(750, 850):
            print("Премия составляет: 40 000")
        elif self.work_hours in range(851, 950):
            print("Премия составляет: 60 000")
        elif self.work_hours > 950:
            print("Премия составляет: 90 000")
        else:
            print("Премия не предусмотрена")


# Данный класс реализует отношение композиции с классом Teacher
class Address:
    # конструктор
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    # строковое представление (перегрузка оператора)
    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)





class Student(Person):

    # переопределяем конструктор базового класса
    def __init__(self, name, study_year, speciality, uni="ITMO"):
        Person.__init__(self, name, uni="ITMO")
        self.study_year = study_year  # устанавливаем год обучения
        self.speciality = speciality  # устанавливаем специальность

    # вывод дополнительной информации на экран
    def display_info(self):
        Person.display_info(self)
        print("Год обучения:", self.study_year, "\tСпециальность:", self.speciality)

    # расчёт стипендии
    def grant (self):
        points = input("Введите оценки за текущий семестр: ").split()
        # преобразовываем элементы списка по одному в числа
        for i in range(len(points)):
            points[i] = float(points[i])
        avg = mean(points)
        print("Средний балл:", avg)
        if avg > 4.5:
            print("Вы обладатель стипендии университета!")
        else:
            print("Недостаточно высокий средний балл. Попробуйте в следующем семестре!")




