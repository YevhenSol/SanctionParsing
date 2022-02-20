from django.db import models
import psycopg2
from psycopg2 import Error

# Create your models here.

class Persons(models.Model):
    def create_func():
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
            # cursor.callproc('sp_fill_crypto_wallet_with_json()')
            #cursor.execute("call sanctions.sp_fill_interest();")
            cursor.execute("call sanctions.sp_fill_entities();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_thing();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_legalentity();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_person();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_address();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_interval();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_value();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_organization();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_identification();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_sanction();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_security();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_other_link();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_vessel();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_asset();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_vehicle();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_airplane();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_associate();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_company();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_crypto_wallet();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_directorships();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_interest();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_family();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_membership();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_ownership();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_passport();")
            connection.commit()
            cursor.execute("call sanctions.sp_fill_representation();")
            connection.commit()

            #result = cursor.fetchall()
            cursor.close()

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection is None:
                    connection.close();
                    print("Соединение с PostgreSQL закрыто")

    create_func()

