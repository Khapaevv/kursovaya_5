import psycopg2
from tabulate import tabulate

class DBManager():


    def __init__(self, database_name, params: dict):
        self.database_name = database_name
        self.params = params


    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        conn = psycopg2.connect(f'dbname={self.database_name}', **self.params)
        with conn.cursor() as cur:
            cur.execute("""
                        SELECT q.employer_name, COUNT(w.vac_hh_id)
                        FROM employers as q
                        JOIN vacancies as w ON q.employer_id = w.employer_id
                        GROUP BY q.employer_name
                        
                        """)
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            headers = ["Company name", "Count of vacancies"]
            result = tabulate(rows, headers=headers)
            return result


    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        conn = psycopg2.connect(f'dbname={self.database_name}', **self.params)
        with conn.cursor() as cur:
            cur.execute("""
                        SELECT q.employer_name, w.vacancy_name, w.salary, w.vacancy_url 
                        FROM employers as q
                        JOIN vacancies as w ON q.employer_id = w.employer_id

                        """)
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            headers = ["employer_name", "vacancy_name", "salary", "vacancy_url"]
            result = tabulate(rows, headers=headers)
            return result


    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        conn = psycopg2.connect(f'dbname={self.database_name}', **self.params)
        with conn.cursor() as cur:
            cur.execute("""
                        SELECT AVG(salary)
                        FROM vacancies
                        WHERE salary <> 0
                        """)
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            headers = ["AVG_salary"]
            result = tabulate(rows, headers=headers)
            return result


    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям"""
        conn = psycopg2.connect(f'dbname={self.database_name}', **self.params)
        with conn.cursor() as cur:
            cur.execute("""
                        SELECT vacancy_name, salary
                        FROM vacancies
                        WHERE salary > (SELECT AVG(salary) FROM vacancies WHERE salary <> 0)
                        """)
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            headers = ["vacancy_name", "salary"]
            result = tabulate(rows, headers=headers)
            return result


    def get_vacancies_with_keyword(self):
        """получает список всех вакансий,
        в названии которых содержатся переданные в метод слова"""
        word = input("Введите слово\n")
        conn = psycopg2.connect(f'dbname={self.database_name}', **self.params)
        with conn.cursor() as cur:
            cur.execute(f"""
                        SELECT * FROM vacancies WHERE vacancy_name LIKE '%{word.lower()}%'
                        """)
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            headers = []
            result = tabulate(rows, headers=headers)
            return result