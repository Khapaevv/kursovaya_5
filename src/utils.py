import requests
import psycopg2
import json
import time
from tqdm import tqdm
from config import config


def create_database(database_name, params: dict):
    """Создание базы данных."""
    params = config()
    conn = psycopg2.connect(database='postgres', **params)
    cur = conn.cursor()
    conn.autocommit = True
    try:
        cur.execute(f"CREATE DATABASE {database_name}")
        print(f"База данных '{database_name}' создана")
    except psycopg2.errors.DuplicateDatabase:
        print('База данных уже существует')
    finally:
        cur.close()
        conn.close()


def create_table_employers(database_name, params: dict):
    """Создание таблицы для сохранения данных о работодателях."""
    conn = psycopg2.connect(f'dbname={database_name}', **params)
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS employers 
                    (
                        employer_id int NOT NULL, 
                        employer_name VARCHAR(255) NOT NULL
                        )
                    """)
        conn.commit()
    conn.close()


def create_table_vacancies(database_name, params: dict):
    """Создание таблицы для сохранения данных о вакансиях."""
    conn = psycopg2.connect(f'dbname={database_name}', **params)
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS vacancies
                    (
                        vacancy_id SERIAL,
                        vac_hh_id int,
                        employer_id int NOT NULL,
                        vacancy_name VARCHAR(255) NOT NULL,
                        vacancy_url TEXT,
                        salary int,
                        schedule VARCHAR(255),
                        CONSTRAINT pk_vacancies_vacancy_id PRIMARY KEY (vacancy_id)
                    );
        """)
        conn.commit()
    conn.close()


def load_table_employers(database_name, params: dict):
    """Наполнение таблицы о работодателях из файла Employers.json."""
    with open('./data/Employers.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    conn = psycopg2.connect(f'dbname={database_name}', **params)
    with conn.cursor() as cur:
        for emp, emp_id in data.items():
            cur.execute(
                'INSERT INTO employers (employer_id, employer_name)'
                'VALUES (%s, %s)', (emp_id, emp))
            conn.commit()
        conn.close()


def load_table_vacancies(database_name, params: dict, url=None):
    """Получение данных с Хед Хантер и наполнение таблицы вакансиями путем перебора employer_id из Employers.json."""
    with open('data/Employers.json', 'r', encoding='utf-8') as file:
        emp_data = json.load(file)
        for emp, employer_id in emp_data.items():
            time.sleep(6)
            url = 'https://api.hh.ru/vacancies?area=113'
            parametrs = {
                'pages': 20,
                'page': 0,
                'per_page': 100
            }
            for page in tqdm(range(20), desc=f'Парсим вакансии {emp}', unit='вакансии', ncols=80,
                             bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}", colour="green"):
                response = requests.get(f'{url}&employer_id={employer_id}&page={page}', parametrs)
                data = response.json()
                conn = psycopg2.connect(f'dbname={database_name}', **params)
                with conn.cursor() as cur:
                    for vac in data['items']:
                        vac_hh_id = vac['id']
                        epm_id = vac['employer']['id']
                        vac_name = vac.get('name')
                        vac_url = vac.get('alternate_url')
                        vac_salary = vac.get('salary')
                        if vac_salary:
                            if vac_salary.get("from") and not vac_salary.get("to"):
                                vac_salary = vac_salary.get("from")
                            elif not vac_salary.get("from") and vac_salary.get("to"):
                                vac_salary = vac_salary.get("to")
                            elif vac_salary.get("from") and vac_salary.get("to"):
                                vac_salary = int((vac_salary.get("from") + vac_salary.get("to")) / 2)
                            elif not vac_salary.get("from") and not vac_salary.get("to"):
                                vac_salary = 0
                        else:
                            vac_salary = 0
                        vac_schedule = vac['schedule']['name']
                        cur.execute(
                            'INSERT INTO vacancies (vac_hh_id, employer_id, vacancy_name, vacancy_url, salary, schedule)'
                            'VALUES (%s, %s, %s, %s, %s, %s)', (vac_hh_id, epm_id, vac_name, vac_url, vac_salary, vac_schedule))
                        conn.commit()
                    conn.close()
