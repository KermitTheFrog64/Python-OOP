from abc import ABC, abstractmethod


# абстрактный класс
class PokerHand(ABC):
    # общий метод, который будут использовать все наследники этого класса
    def show(self):
        print("Show your hand")

    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def chance(self):
        pass


# класс-миксин
class GainMixin:
    def count_gain(self):
        amount = int(input("Enter the amount of chips: "))
        price = int(input("Enter the price of one chip: "))
        print("Your gain is: ", amount*price)


# с помощью данного класса было реализовано множественное наследование
class Pass:
    def refrain (self):
        move = input("What is your next move? (check/bet/pass/raise) ")
        if move == "check":
            print("Checking")
        elif move == "bet":
            print("Betting")
        elif move == "pass":
            print("Passing")
        else:
            print("Raising")


# классы-наследники от абстрактного класса PokerHand
class HighCard(PokerHand, GainMixin, Pass):
    def chance(self):
        print("A chance of making a combination: 0,1741192")


class Pair(PokerHand, GainMixin, Pass):
    def chance(self):
        print("A chance of making a combination: 0,43822546")


class TwoPair(PokerHand, GainMixin, Pass):
    def chance(self):
        print("A chance of making a combination: 0,23495536")


class ThreeOfaKind(PokerHand, GainMixin, Pass):
    def chance(self):
        print("A chance of making a combination: 0,04829870")


class Straight(PokerHand, GainMixin, Pass):
    def chance(self):
        print("A chance of making a combination: 0,04619382")


class Flush(PokerHand, GainMixin, Pass):
    def chance(self):
        print("A chance of making a combination: 0,03025494")


class FullHouse(PokerHand, GainMixin, Pass):
    def chance(self):
        print("A chance of making a combination: 0,02596102")


class FourOfAKind(PokerHand, GainMixin, Pass):
    def chance(self):
        print("A chance of making a combination: 0,00168067")


class StraightFlush(PokerHand, GainMixin, Pass):
    def chance(self):
        print("A chance of making a combination: 0,00027851")


class RoyalFlush(PokerHand, GainMixin, Pass):
    def chance(self):
        print("A chance of making a combination: 0,00003232")

