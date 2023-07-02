import json


def areas(name: str) -> int:
    """Функция для обрабоки субъектов рф
    и выдачи указанного пользователем"""
    with open('areas.json', 'r') as f:
        ss = json.load(f)
        for i in ss:
            if name.title() in i['name']:
                return i['id']



