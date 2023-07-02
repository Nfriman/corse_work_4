from scr.parsing_hh import Parsing_hh
from scr.functions import areas
import json


def user_interaction():
    """функцию для взаимодействия с пользователем"""
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода : "))
    aras = areas(input('Субъекты страны: '))
    salary = int(input('Предпочитаемая заработная плата: '))
    usre = Parsing_hh(search_query, top_n, aras, salary)
    usre.parsing()
    usre.get_json()

    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        caount = 0
        for i in data:
            caount += 1
            print(f'Вакансия № {caount} зарабатная плата {i["salary"]}')
            print(f"{i['name']} заработная плата {i['salary']}")
            print(i['experience'])
            print(f"{i['address']}. Cсылка на вакансию {i['url']}")
            print()



if __name__ == "__main__":
    user_interaction()