# Я выбрала данный пример, т.к. он хорошо показывает разницу между синронным и асинхронным иполнением программы

import random
from time import sleep
import asyncio


def task(pid):
    # симуляция задержки в выполнении программы на сгенерированное время
    sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)


#  синхронное выполнение функции task
def synchronous():
    for i in range(1, 10):
        task(i)


# Сопрограмма
async def task_coro(pid):
    # приостанавливаем асинхронную задачу на сгенерированное время
    await asyncio.sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)


async def asynchronous():
    # создаём и планируем асинхронный запуск задач
    tasks = [asyncio.ensure_future(task_coro(i)) for i in range(1, 10)]
    # запускаем созданные задачи
    await asyncio.wait(tasks)


print('Synchronous:')
synchronous()

# получаем текущий цикл событий
ioloop = asyncio.get_event_loop()
print('Asynchronous:')
# запуск данного цикла
ioloop.run_until_complete(asynchronous())
# очищаем все очереди и остановливаем Исполнителя
ioloop.close()