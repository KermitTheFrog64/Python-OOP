import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')  # подключение к БД
    # подготавливаем запрос создания таблицы
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS sqlitedb_developers (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    joining_date datetime,
                                    salary REAL NOT NULL);'''

    cursor = sqlite_connection.cursor()  # С помощью объекта соединения создается объект cursor, который позволяет выполнять SQLite-запросы из Python
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)  # выполняем запрос в БД
    sqlite_connection.commit()
    print("Таблица SQLite создана")
    cursor.close()  # закрываем соединение с базой и объектом cursor

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")


def insert_variable_into_table(dev_id, name, email, join_date, salary):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        #  INSERT-запрос для вставки данных в таблицу
        sqlite_insert_with_param = """INSERT INTO sqlitedb_developers
                              (id, name, email, joining_date, salary)
                              VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (dev_id, name, email, join_date, salary)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()  # сохраняем изменения ав БД
        print("Переменные Python успешно вставлены в таблицу sqlitedb_developers")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


choice = "y"
while choice.lower() == "y":
    print("Введите данные:")
    ID = input("Введите ID: ")
    NAME = input("Введите имя: ")
    EMAIL = input("Введите Email: ")
    DATE = input("Введите дату начала работы: ")
    SALARY = input("Введите ЗП: ")
    insert_variable_into_table(ID, NAME, EMAIL, DATE, SALARY)

    choice = input("Для продолжения нажмите Y, а для выхода любую другую клавишу: ")
print("Ввод данных закончен")