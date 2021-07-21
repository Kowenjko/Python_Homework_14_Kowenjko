import psycopg2
from psycopg2 import Error
from settings import *

try:
    connection = psycopg2.connect(user=USER,
                                  password=PASSWORD,
                                  host=HOST,
                                  port=PORT,
                                  database='shop_db')
    cursor = connection.cursor()
# -----------------Таблиці------------------------------------
    # login = """CREATE TABLE login
    #                       (ID SERIAL  PRIMARY KEY,
    #                        login      varchar(50)    NOT NULL,
    #                        password   varchar(50)    NOT NULL,
    #                        role       varchar(50)    NOT NULL
    #                        ); """
    # cursor.execute(login)
    # connection.commit()
# ----------------------------------------------------------------
    insert_login = """ INSERT INTO  login (ID, login, password,role)
                                     VALUES
                                     (1, 'admin','admin','admin'),
                                     (2, 'roman','1234','employee'),
                                     (3, 'logo','2564','employee'),
                                     (4, 'kolis','457','customer'),
                                     (5, 'lims','1236','customer')                                    

                    """
    cursor.execute(insert_login)
    connection.commit()
# ----------------------------------------------------------------

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
