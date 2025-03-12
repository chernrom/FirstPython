import mysql.connector

try:
    with mysql.connector.connect(
        user='romchich', password='t4n-zED-erA-MEH',
        host='db4free.net', database='myfirstpython314') as sql_connection:
        query_str = 'select name1, number2 from first_table'
        sql_cursor = sql_connection.cursor()
        sql_cursor.execute(query_str)

        for (name1, number2) in sql_cursor:
            print(f'number: {number2}, name: {name1}')
except mysql.connector.errors.Error as err:
    print(err)