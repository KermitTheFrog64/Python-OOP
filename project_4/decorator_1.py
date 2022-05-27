def benchmark(func):  # декоратор, замеряющий время выполнения функции
    import time

    def wrapper():  # функция-обёртка
        start = time.time()  # сохраняем время перед выполнением обёрнутой функции
        func()  # выполняем функцию
        end = time.time()  # снова сохраняем текущее время
        print('[*] Время выполнения: {} секунд.'.format(end - start))  # вычитаем из текущего времени начальное

    return wrapper


@benchmark  # функция-декоратор
def fetch_webpage():  # функция, делающая GET-запрос к главной странице Google
    import requests
    webpage = requests.get('https://google.com')


fetch_webpage()


'''def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)'''