import requests
import psycopg2
import json

def load_table_employers():
    with open('data/Employers.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    conn = psycopg2.connect(host='localhost', database='KR_5', user='postgres', password='Py091105')
    with conn.cursor() as cur:
        for emp, emp_id in data.items():
            cur.execute(
                        'INSERT INTO employers (employer_id, employer_name)'
                        'VALUES (%s, %s)', (emp_id, emp))
            conn.commit()
        conn.close()

def load_table_vacancy(employer_id, url=None):
    """Метод вытаскивает работодателя по employer_id (только по России)
    и складывает в отдельный json для каждого работодателя"""
    url = 'https://api.hh.ru/vacancies?area=113'
    params = {
        'page': 0,
        'per_page': 100
    }
    response = requests.get(f'{url}&employer_id={employer_id}', params)
    data = response.json()
    conn = psycopg2.connect(host='localhost', database='KR_5', user='postgres', password='Py091105')
    with conn.cursor() as cur:
        for vac in data['items']:
            print(vac)
            print()
            vac_params = []
            vac_id = vac['id']
            vac_params.extend(vac_id)
            cur.execute(
                'INSERT INTO vacancies (vac_hh_id, employer_id, vacancy_name)'
                'VALUES (%s, %s, %s)', (102601909, 1740, 'Аналитик (Python/C++)'))
            conn.commit()
        conn.close()




            # print(vac)
            # print()

        # items
        # found
        # pages
        # page
        # per_page
        # clusters
        # arguments
        # fixes
        # suggests
        # alternate_url
        # print(data)
        # with open(f"./data/Employers/{self.employer_name}_employer.json", "w", encoding='utf-8') as file:
        #     data_2 = json.loads(data_1)
        #     print(data_2)
            # data_dump = json.dump(data, file, sort_keys=True, indent=4, ensure_ascii=False)
            # for vac in data_dump:


# def create_class_from_json():
#     """Создает экземпляры класса HH_employer из Employers.json и использует load_employer()"""
#     with open('data/Employers.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#         for employer_name, employer_id in data.items():
#
#             HH_employer(f"{employer_name}", f"{employer_id}").load_employer()




if __name__ == "__main__":
    # create_class_from_json()
    # load_employer()
    # load_table_employers()
    load_table_vacancy('1740')



    # create_class_from_json()
    # Yandex = HH_employer('Yandex', '1740')
    # Yandex.load_table_vacancy()
    # print(Yandex.__repr__())
    # VK = HH_employer('VK', '15478')
    # Rosteh = HH_employer('Rosteh', '4986323')
    # Tbank = HH_employer('Tbank', '78638')
    # Sberbank = HH_employer('Sberbank', '3529')
    # Rostelecom = HH_employer('Rostelecom', '2748')
    # MTS = HH_employer('MTS', '3776')
    # Kaspersky = HH_employer('Kaspersky', '1057')
    # Avito = HH_employer('Avito', '84585')
    # Ozon = HH_employer('Ozon', '2180')
    #
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