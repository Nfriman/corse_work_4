from abc import ABC, abstractmethod


class AbsParsing(ABC):

    """Абстрактный класс"""

    @abstractmethod
    def parsing(self):
        '''Абстактный метод для обрабоки данных'''
        pass

    @abstractmethod
    def get_json(self):
        '''Абстактный метод для  добавления вакансий в json файл'''
        pass