import requests
import json
from abc import ABC, abstractmethod


class AbsParsing(ABC):
    """Абстрактный класс для вывода вакансий на hh.ru"""
    @abstractmethod
    def parsing(self):
        '''Абстактный метод для обрабоки данных'''
        pass

    @abstractmethod
    def get_json(self):
        '''Абстактный метод для  добавления вакансий в json файл'''
        pass


class Parsing_hh(AbsParsing, ABC):
    """ класс для парсинга вакансий на сайте hh.ru """
    list_vacancy = []

    def __init__(self, text: str, caount_vacan: int, area: int, salary: int):
        self.salary = salary  # огр. пользывателя мин. платы
        self.text = text  # ключевые слово для опр. вакансий
        self.caount_vacan = caount_vacan  # кол. вакансий на вывод
        self.area = area  # номер субъекта
        self.url = f'https://api.hh.ru/vacancies?&only_with_salary=true&salary={self.salary}'  # АПИ сайта

    def parsing(self):
        """ метод для получения АПИ с указанными параметрами его обработка и получения словаря с нужными данными"""
        parms = {"area": self.area,
                 "per_page": self.caount_vacan,
                 "text": self.text}
        hh = requests.get(self.url, parms).json()

        for index in hh['items']:
            name = index['name']  # название вакансии
            url = index['alternate_url']  # ссылка на вакансию
            experience = index['snippet']['requirement']  # опыт работы
            salary = f"от {index['salary']['from']} до {index['salary']['to']}"  # ЗП от и до

            if index['address'] != None:
                address = index['address']['raw']  # адрес офиса
            else:
                address = 'Нет адреса'

            self.list_vacancy.append({"name": name, "salary": salary, 'url': url, 'experience': experience, 'address': address})

        return self.list_vacancy

    def get_json(self):
        ''' функция для добавленния данных в json файл '''

        with open('data.json', 'w', encoding='utf-8') as outfile:
            json.dump(self.list_vacancy, outfile, ensure_ascii=False, sort_keys=True)


