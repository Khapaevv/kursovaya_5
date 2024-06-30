import requests
import json



class HH_employer():
    """Класс для работы с API HeadHunter России"""

    def __init__(self, employer_name, employer_id):
        self.employer_name = employer_name
        self.employer_id = employer_id


    def load_employer(self, url=None):
        """Метод вытаскивает вакансии по ключевому
        слову вакансии (только по России) и складывает в json"""
        url = 'https://api.hh.ru/vacancies?area=113'
        params = {
            'page': 0,
            'per_page': 100
        }
        response = requests.get(f'{url}&employer_id={self.employer_id}', params)
        data = response.json()
        with open(f"./data/{self.employer_name}_employer.json", "w", encoding='utf-8') as file:
            json.dump(data, file, sort_keys=True, indent=4, ensure_ascii=False)
        return data

if __name__ == "__main__":
    Yandex = HH_employer('Yandex', '1740')
    VK = HH_employer('VK', '15478')
    Rosteh = HH_employer('Rosteh', '4986323')
    Tbank = HH_employer('Tbank', '78638')
    Sberbank = HH_employer('Sberbank', '3529')
    Rostelecom = HH_employer('Rostelecom', '2748')
    MTS = HH_employer('MTS', '3776')
    Kaspersky = HH_employer('Kaspersky', '1057')
    Avito = HH_employer('Avito', '84585')
    Ozon = HH_employer('Ozon', '2180')

    Yandex.load_employer()
    VK.load_employer()
    Rosteh.load_employer()
    Tbank.load_employer()
    Sberbank.load_employer()
    Rostelecom.load_employer()
    MTS.load_employer()
    Kaspersky.load_employer()
    Avito.load_employer()
    Ozon.load_employer()





