import datetime

import psycopg2
from psycopg2 import Error
import fileData


def conn():
    try:
        connection = psycopg2.connect(user="pgremote",
                                      password="fglP04hXfq",
                                      host="92.53.75.44",
                                      port="5432",
                                      database="sap_data")

        cursor = connection.cursor()
        begin_time = datetime.datetime.now()
        postgresql_select_query = \
            f"select data->>'MATNR', data->>'VKORG', data->>'WHOLESALE'" \
            f" from ms_materials_store where data->>'VKORG' = '1000'"
        cursor.execute(postgresql_select_query)
        records = cursor.fetchall()
        print(datetime.datetime.now()-begin_time)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
            print(f'Количество записей - {len(records)}')

conn()
def process():
    records=conn()
    for row in records:
       if row[2]=='X':
            fileData.addRecord(row[0],row[1], True)
       if row[2]=='':
           fileData.addRecord(row[0], row[1], False)