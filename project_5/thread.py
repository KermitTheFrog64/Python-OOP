import threading


def output(x, event_for_wait, event_for_set):
    for i in range(10):
        event_for_wait.wait()  # ждём, пока флаг не будетустановлен
        event_for_wait.clear()  # сбрасываем внутренний флаг
        print(x)
        event_for_set.set()  # устанавливаем внутренний флаг


# создаём объекты Event
event1 = threading.Event()
event2 = threading.Event()

# создаём потоки
thread1 = threading.Thread(target=output, args=(0, event1, event2))
thread2 = threading.Thread(target=output, args=(1, event2, event1))

# запускаем потоки
thread1.start()
thread2.start()

event1.set()  # устанавливаем внутренний флаг

# поток по завершении присоединяется к вызывающему метод потоку
thread1.join()
thread2.join()
