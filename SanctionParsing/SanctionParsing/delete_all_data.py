import psycopg2
from psycopg2 import Error
from django.db import connection


def delete_all_data():
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="admin",
                                      # пароль, который указали при установке PostgreSQL
                                      password="admin",
                                      host="localhost",
                                      port="5432",
                                      database="sanctions")

        cursor = connection.cursor()
        # хранимая процедура
        #arg = 5
        cursor.execute("SELECT sanctions.fn_delete_all_data_from_tables();")#, (arg))
        connection.commit()
        #result = cursor.fetchall()
        cursor.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection is None:
                connection.close();
                print("Соединение с PostgreSQL закрыто")

delete_all_data()

