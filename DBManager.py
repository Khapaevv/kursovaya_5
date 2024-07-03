import psycopg2
import self


class DBManager():
    pass

    def __init__(self, host='localhost', database='KR_5', user='postgres', password='Py091105'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password


    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute("""
                        SELECT DISTINCT employer_id FROM vacancies
                        """)
            employers_list = cur.fetchall()
            print(employers_list)
            # for employer_name, employer_id in employers_list.items():
            #     print(employer_id)

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        pass


    def get_avg_salary():
        """получает среднюю зарплату по вакансиям"""
        pass


    def get_vacancies_with_higher_salary():
        """получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям"""
        pass


    def get_vacancies_with_keyword(self):
        """получает список всех вакансий,
        в названии которых содержатся переданные в метод слова, например python"""
        pass

if __name__ == "__main__":
    KR_5 = DBManager()
    KR_5.get_companies_and_vacancies_count()