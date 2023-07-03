import json


def areas(name: str) -> int:
    """Функция для обрабоки субъектов рф  из списка areas.json
    и выдачи номера субъекта указанного пользователем"""
    with open('areas.json', 'r') as f:
        area = json.load(f)
        for i in area:
            if name.title() in i['name']:
                return i['id']


