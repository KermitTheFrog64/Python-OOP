from __future__ import annotations
from abc import ABC, abstractmethod


# Класс логистики объявляет фабричный метод, который должен возвращать объект
# класса Transport
class Logistics(ABC):
    # фабричный метод
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self) -> str:
        # Вызываем фабричный метод, чтобы получить объект-транспорт.
        transport = self.create_transport()

        # Далее, работаем с этим продуктом.
        result = f"Creator: The same creator's code has just worked with {transport.deliver()}"

        return result


# Классы-наследники переопределяют фабричный метод для того, чтобы изменить тип
# итогового транспорта
class RoadLogistics(Logistics):
    # Cигнатура метода по-прежнему использует тип
    # абстрактного продукта, хотя фактически из метода возвращается конкретный
    # продукт. Таким образом, класс логистики может оставаться независимым от конкретных
    # классов продуктов.
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


# Интерфейс Транспорта объявляет операции, которые должны выполнять все
# конкретные виды транспорта
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


#Конкретные виды транспорта предоставляют различные реализации интерфейса Транспорта.
class Truck(Transport):
    def deliver(self) -> str:
        return "{Result of the Truck}"


class Ship(Transport):
    def deliver(self) -> str:
        return "{Result of the Ship}"


# Клиентский код работает с экземпляром конкретного отдела логистики через
# его базовый интерфейс. Пока клиент продолжает работать с логистикой через
# базовый интерфейс, вы можете передать ему любой подкласс логистики.
def client_code(creator: Logistics) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.plan_delivery()}", end="")


if __name__ == "__main__":
    print("App: Launched with the RoadLogistics.")
    client_code(RoadLogistics())
    print("\n")

    print("App: Launched with the SeaLogistics.")
    client_code(SeaLogistics())