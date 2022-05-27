import random


# определение пользовательских исключений
# Базовый класс для других исключений
class Error(Exception):
    pass


# Вызывается, когда входное значение мало
class ValueTooSmallError(Error):
    pass


# Вызывается, когда входное значение велико
class ValueTooLargeError(Error):
    pass


# число попыток
guesses_made = 0

# получаем имя пользователя из консольного ввода
name = input('Hello, what is your name\n')

# получаем случайное число в диапазоне от 1 до 10, где каждое число соответствует покерной комбинации
number = random.randint(1, 10)

print('Well, {0}, I thought of a number between 1 and 10. Can you guess?'.format(name))
print('1 is for Royal Flash\n' '2 is for Straight Flush\n' 
      '3 is for Four of a kind\n' '4 is for Full House\n' 
      '5 is for Flush\n' '6 is for Straight\n' '7 is for Three of a kind\n' 
      '8 is for Two pair\n' '9 is for Pair\n' '10 is for High card\n')


# игра продолжается до тех пор, пока пользователь не угадает комбинацию
while True:
    try:
        guess = int(input("Ввести число: "))
        guesses_made += 1
        if guess < number:
            raise ValueTooSmallError
        elif guess > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This number is less than the guessed number, please try again!\n")
    except ValueTooLargeError:
        print("This number is greater than the guessed number, please try again!\n")

print("Congratulations! You guessed right.")


