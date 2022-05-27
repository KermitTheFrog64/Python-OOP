from enum import Enum, auto
from abc import ABC, abstractmethod
from collections import namedtuple

'''Фабричный метод'''

# перечисление текущих рецептов пицц, которые можно приготовить
class PizzaType(Enum):
    MARGARITA = 0,
    MEXICO = 1,
    STRACATELLA = 2


# базовый класс для пицц, которые можно приготовить в пиццерии
class Pizza:
    def __init__(self, price: float):
        self.__price = price  # цена пиццы

    def get_price(self) -> float:  # метод, возвращающий пиццу
        return self.__price


# производные классы
class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(350)


class PizzaMexico(Pizza):
    def __init__(self):
        super().__init__(420)


class PizzaStracatella(Pizza):
    def __init__(self):
        super().__init__(450)


# фабричный метод
def create_pizza(pizza_type: PizzaType) -> Pizza:
    # словарь (в качестве ключа выступает перечисление,
    # а значение - тип класса конкретной пиццы)
    factory_dict = {
        PizzaType.MARGARITA: PizzaMargarita,
        PizzaType.MEXICO: PizzaMexico,
        PizzaType.STRACATELLA: PizzaStracatella
    }
    return factory_dict[pizza_type]()  # возвращаем экземпляр класса, соответствующий ключу и его конструктор


'''Строитель'''

# именованный кортеж для свойств основы пиццы
PizzaBase = namedtuple('PizzaBase', ['DoughDepth', 'DoughType'])


# перечисления видов теста
class PizzaDoughType(Enum):
    WHEAT = auto()
    CORN = auto()
    RYE = auto()


# перечисления толщины пиццы
class PizzaDoughDepth(Enum):
    THIN = auto()
    THICK = auto()


# перечисления видов соуса
class PizzaSauceType(Enum):
    PESTO = auto()
    WHITE_GARLIC = auto()
    BARBEQUE = auto()
    TOMATO = auto()


# перечисления видов топпинга
class PizzaTopLevelType(Enum):
    MOZZARELLA = auto()
    SALAMI = auto()
    BACON = auto()
    MUSHROOMS = auto()
    SHRIMPS = auto()


# класс компонуемого продукта (пиццы)
class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
        self.cooking_time = None

    def __str__(self): # перегружаем метод str
        info: str = f"Pizza name: {self.name} \n" \
                    f"dough type: {self.dough.DoughDepth.name} & " \
                    f"{self.dough.DoughType.name} \n" \
                    f"sauce type: {self.sauce} \n" \
                    f"topping: {[it.name for it in self.topping]} \n" \
                    f"cooking time: {self.cooking_time} minutes"
        return info


# абстрактный класс, задающий интерфейс строителя
class Builder(ABC):

    @abstractmethod
    def prepare_dough(self) -> None: pass

    @abstractmethod
    def add_sauce(self) -> None: pass

    @abstractmethod
    def add_topping(self) -> None: pass

    @abstractmethod
    def get_pizza(self) -> Pizza: pass


# реализация конкретных строителей для сборки пиццы
class MargaritaPizzaBuilder(Builder):

    def __init__(self):
        self.pizza = Pizza("Margarita")
        self.pizza.cooking_time = 15

    def prepare_dough(self) -> None:
        self.pizza.dough = PizzaBase(PizzaDoughDepth.THICK, PizzaDoughType.WHEAT)

    def add_sauce(self) -> None:
        self.pizza.sauce = PizzaSauceType.TOMATO

    def add_topping(self) -> None:
        self.pizza.topping.extend(
            [
                it for it in (PizzaTopLevelType.MOZZARELLA,
                              PizzaTopLevelType.MOZZARELLA,
                              PizzaTopLevelType.BACON
                              )
            ]
        )

    def get_pizza(self) -> Pizza:
        return self.pizza


class SalamiPizzaBuilder(Builder):

    def __init__(self):
        self.pizza = Pizza("Salami")
        self.pizza.cooking_time = 10

    def prepare_dough(self) -> None:
        self.pizza.dough = PizzaBase(PizzaDoughDepth.THIN, PizzaDoughType.RYE)

    def add_sauce(self) -> None:
        self.pizza.sauce = PizzaSauceType.BARBEQUE

    def add_topping(self) -> None:
        self.pizza.topping.extend(
            [
                it for it in (PizzaTopLevelType.MOZZARELLA,
                              PizzaTopLevelType.SALAMI
                              )
            ]
        )

    def get_pizza(self) -> Pizza:
        return self.pizza


# класс Директор, отвечающий за процесс поэтапного приготовления пиццы
class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):  # передаём экземпляр класса Строитель и приводим к базовому интерфейсу
        self.builder = builder

    def make_pizza(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.prepare_dough()
        self.builder.add_sauce()
        self.builder.add_topping()


if __name__ == '__main__':
    for pizza in PizzaType:  # итерация по перечислениям
        my_pizza = create_pizza(pizza)
        print(f'Pizza type: {pizza}, price: {my_pizza.get_price()}')
    director = Director()  # создаём экземпляр класса Директор
    for it in (MargaritaPizzaBuilder, SalamiPizzaBuilder): # цикл по конкретным классам Строителя
        builder = it()  # создаём экземпляр класса
        director.set_builder(builder)  # передаём Директору
        director.make_pizza()  # вызываем метод, создающий пиццу
        pizza = builder.get_pizza()  # возвращаем скомпонованный экземпляр класса Пицца
        print(pizza)
        print('--------------------------------')