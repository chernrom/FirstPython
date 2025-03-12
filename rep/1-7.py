# Открываем файл на запись
with open('file.txt', 'w') as file:
    # Записываем 7 строк с номерами
    for i in range(1, 8):
        file.write(f"Строка номер {i}\n")

import json

# Создаём массив из семи чисел
numbers = [1, 2, 3, 4, 5, 6, 7]

# Превращаем массив в JSON-строку
json_data = json.dumps(numbers)

# Сохраняем JSON в файл
with open('numbers.json', 'w') as file:
    file.write(json_data)

import mysql.connector

# Данные для подключения к базе данных
user = 'romchich'
password = 't4n-zED-erA-MEH'
host = 'db4free.net'
database = 'myfirstpython314'

# Данные для заполнения таблицы
days_of_week = [
    ("Понедельник", 1),
    ("Вторник", 2),
    ("Среда", 3),
    ("Четверг", 4),
    ("Пятница", 5),
    ("Суббота", 6),
    ("Воскресенье", 7)
]

try:
    # Подключаемся к базе данных
    with mysql.connector.connect(user=user, password=password, host=host, database=database) as sql_connection:
        # Создаём курсор
        sql_cursor = sql_connection.cursor()

        # Выполняем запрос на заполнение таблицы
        query = "INSERT INTO first_table (day_name, day_number) VALUES (%s, %s)"
        sql_cursor.executemany(query, days_of_week)

        # Применяем изменения
        sql_connection.commit()

except mysql.connector.errors.Error as err:
    print(err)
