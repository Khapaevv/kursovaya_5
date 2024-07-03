import json
from utils import create_table_employers, create_table_vacancies, load_table_employers, load_table_vacancy


def main():
    print("Привет дорогой друг!")
    start_word = input("Если хочешь начать - введи 'Поехали'\n")
    start_word_lower = start_word.lower()
    if start_word_lower == "поехали":
        print("Я отобрал и сохранил для тебя 10 лучших IT компаний, с ними мы и будем работать")
        print("")
    else:
        print("Не верно, начинай с начала")
    # # Создание таблицы для сохранения данных о работодателях.
    # create_table_employers()
    # # Создание таблицы для сохранения данных о вакансиях.
    # create_table_vacancies()
    # # Наполнение таблицы о работодателях из файла Employers.json.
    # load_table_employers()
    # # Получение данных с Хед Хантер и наполнение таблицы вакансиями путем перебора employer_id из Employers.json.
    # load_table_vacancy()



if __name__ == "__main__":
    main()
    # create_table_employers()
    # create_table_vacancies()
    # load_table_employers()
    # load_table_vacancy()


