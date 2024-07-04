from src.utils import *
from config import config
from src.DBManager import DBManager

def main():
    print("Здравствуйте!")
    start_word = input("Для того, чтобы начать - введите (да/нет): \n").lower()
    if start_word == 'да':
        print("Я отобрал и сохранил для Вас 10 интересных компаний, с ними мы и будем работать")
        print("Вам необходимо в файл database.ini ввести данные для подключения к Вашему postgresql")
        params = config()
        database_name = input("Если изменили database.ini, то введите название базы данных: ")
        create_database(database_name, params)
        print("В базе данных создаем таблицы employers и vacancies")
        create_table_employers(database_name, params)
        create_table_vacancies(database_name, params)
        print("Наполняем таблицы данными, придется подождать :)")
        load_table_employers(database_name, params)
        load_table_vacancies(database_name, params)
        print("Спасибо за ожидание, наполнение прошло успешно")
        print("Хотите получить список всех компаний и количество вакансий у каждой компании?")
        key = input("Если да, то введите (да/нет): \n").lower()
        if key == "да":
            dbmanager = DBManager(database_name, params)
            print(dbmanager.get_companies_and_vacancies_count())
        else:
            print("Может нужно узнать что-то другое?")
        print("Хотите получить список вакансий с указанием названия компании, зарплаты и ссылки на вакансию?")
        key_2 = input("Если да, то введите (да/нет): \n").lower()
        if key_2 == "да":
            dbmanager = DBManager(database_name, params)
            print(dbmanager.get_all_vacancies())
        else:
            print("Может нужно узнать что-то другое?")
        print("Хотите получить среднюю зарплату по вакансиям?")
        key_3 = input("Если да, то введите (да/нет): \n").lower()
        if key_3 == "да":
            dbmanager = DBManager(database_name, params)
            print(dbmanager.get_avg_salary())
        else:
            print("Может нужно узнать что-то другое?")
        print("Хотите получить список всех вакансий,у которых зарплата выше средней по всем вакансиям?")
        key_4 = input("Если да, то введите (да/нет): \n").lower()
        if key_4 == "да":
            dbmanager = DBManager(database_name, params)
            print(dbmanager.get_vacancies_with_higher_salary())
        else:
            print("Может нужно узнать что-то другое?")
        print("Хотите получить список всех вакансий,в названии которых содержатся переданные в метод слова?")
        key_5 = input("Если да, то введите (да/нет): \n").lower()
        if key_5 == "да":
            dbmanager = DBManager(database_name, params)
            print(dbmanager.get_vacancies_with_keyword())
        else:
            print("На этом все!")
    else:
        print("Не верно, начнайте все с начала")


if __name__ == "__main__":
    main()


