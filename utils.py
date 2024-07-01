import json
import psycopg2






def create_database():
    """Создание базы данных и таблиц для сохранения данных о работодателях и вакансиях."""

    conn = psycopg2.connect(
        host='localhost',
        database='KR_5',
        user='postgres',
        password='Py091105'
    )

    # conn.autocommit = True
    cur = conn.cursor()

    cur.execute("DROP TABLE employers CASCADE")
    # cur.execute(f"CREATE DATABASE KR_5")
    conn.commit()
    conn.close()

#     conn = psycopg2.connect(host='localhost', database='KR_5', user='postgres', password='Py091105')
#
#     with conn.cursor() as cur:
#         cur.execute("""
#                     CREATE TABLE employers
#                     (
#                         id SERIAL,
#                         employer_id int PRIMARY KEY,
#                         employer_name VARCHAR(255) NOT NULL,
#                         employer_url TEXT
#                     )
#                     """)
#
#     with conn.cursor() as cur:
#         cur.execute("""
#             CREATE TABLE videos (
#                 video_id SERIAL PRIMARY KEY,
#                 channel_id INT REFERENCES channels(channel_id),
#                 title VARCHAR NOT NULL,
#                 publish_date DATE,
#                 video_url TEXT
#             )
#         """)
#
#     conn.commit()
#     conn.close()



# if __name__ == "__main__":
    # create_database()
    # Yandex = HH_employer('Yandex', '1740')
    # VK = HH_employer('VK', '15478')
    # Rosteh = HH_employer('Rosteh', '4986323')
    # Tbank = HH_employer('Tbank', '78638')
    # Sberbank = HH_employer('Sberbank', '3529')
    # Rostelecom = HH_employer('Rostelecom', '2748')
    # MTS = HH_employer('MTS', '3776')
    # Kaspersky = HH_employer('Kaspersky', '1057')
    # Avito = HH_employer('Avito', '84585')
    # Ozon = HH_employer('Ozon', '2180')

    # Yandex.load_employer()
    # VK.load_employer()
    # Rosteh.load_employer()
    # Tbank.load_employer()
    # Sberbank.load_employer()
    # Rostelecom.load_employer()
    # MTS.load_employer()
    # Kaspersky.load_employer()
    # Avito.load_employer()
    # Ozon.load_employer()
    #
    # create_class_from_json()
    # create_class_from_json().load_employer()


