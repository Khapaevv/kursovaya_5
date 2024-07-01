import psycopg2


def create_tables():
    """Создание таблиц для сохранения данных о работодателях и вакансиях."""
    conn = psycopg2.connect(host='localhost', database='KR_5', user='postgres', password='Py091105')

    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS employers 
                    (
                        employer_id int, 
                        employer_name VARCHAR(255) NOT NULL, 
                        employer_url TEXT,
        
                        CONSTRAINT pk_employer_id PRIMARY KEY (employer_id)
                    );
                    """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS vacancies
            (
                vacancy_id SERIAL,
                employer_id int NOT NULL,
                vacancy_name VARCHAR(255) NOT NULL,
                vacancy_url TEXT,
                salary int,
                currency VARCHAR(3),
                shedule VARCHAR(255),
                
                CONSTRAINT pk_vacancies_vacancy_id PRIMARY KEY (vacancy_id)
            );
            ALTER TABLE vacancies ADD CONSTRAINT fk_vacancies_employers FOREIGN KEY(employer_id) REFERENCES employers(employer_id);
        """)

    conn.commit()
    conn.close()

def fill_tables():
    """Наполнение таблиц из json файлов каждого работодателя"""

    conn = psycopg2.connect(host='localhost', database='KR_5', user='postgres', password='Py091105')






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
