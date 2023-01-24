import doctest


class Notebook:
    def __init__(self, pages: (int, float), height: (int, float), length: (int, float)):
        if not isinstance(length, (int, float)):
            raise TypeError
        if length <= 0:
            raise ValueError
        self.length = length  # длина блокнота

        if not isinstance(height, (int, float)):
            raise TypeError
        if height <= 0:
            raise ValueError
        self.height = height  # высота блокнота

        if not isinstance(pages, (int, float)):
            raise TypeError
        if pages < 0:
            raise ValueError
        self.pages = pages

    def tear_out_pages(self, tear_out: (int, float)):
        if not isinstance(tear_out, (int, float)):
            raise TypeError
        if tear_out < 0:
            raise ValueError
        ...
    def notebook_is_square(self):
        '''
        Является ли блокнот квадратным
        :return: True / False
        '''
        ...
if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass


class HotelChecking:
    def __init__(self, people: (int), lux: (int, float), econom: (int, float)):
        if not isinstance(people, int):
            raise TypeError
        if people < 0:
            raise ValueError
        self.people = people

        if not isinstance(lux, (int, float)):
            raise TypeError
        if lux <= 0:
            raise ValueError
        self.lux = lux

        if not isinstance(econom, (int, float)):
            raise TypeError
        if econom <= 0:
            raise ValueError
        self.econom = econom

    def rooms_availiable(self, rooms: int):
        '''
        Есть ли нужное количество свободных номеров
        :param rooms: Количество свободных номеров
        Пример:
        rooms = Avaliable(10, 20)
        rooms.rooms_avaliable(1, 2)
        :return: True / False
        '''
        if not isinstance(rooms, int):
            raise TypeError
        if rooms < 0:
            raise ValueError
        ...
    def buy_rooms(self, buy: (int, float)):
        '''
        Сможем ли мы оплатить нужное количество номеров
        :param buy: Количество денег
        Пример:
        buy = Money(50000)
        buy.buy_rooms(40000)
        :return: True / False
        '''
        if not isinstance(buy, (int, float)):
            raise TypeError
        if buy < 0:
            raise ValueError
        ...

class Pizza:
    def __init__(self, diameter: (int, float), ingridients: list, weight: (int,float)):
        if not isinstance(diameter, (int, float)):
            raise TypeError
        if diameter < 0:
            raise ValueError
        self.diameter = diameter

        if not isinstance(ingridients, list):
            raise TypeError
        self.dingridients = ingridients

        if not isinstance(weight, (int, float)):
            raise TypeError
        if weight <= 0:
            raise ValueError
        self.weight = weight

    def add_ingridient_(self, ingridient_ordered: str):
        '''
        Возможно ли добавить дополнительный ингридиент при заказе
        Проверяет, есть ли такой продукт в списке ингридиентов
        :param ingridient_: ингридиент, который нужно добавить
        Пример:
        ingridient_ordered = ingridient_ordered(сыр)
        ingridient_ordered.add_ingridient_(сыр)
        :return: True / False
        '''
        if not isinstance(ingridient_ordered, str):
            raise None
        self.ingridient_ordered = ingridient_ordered
        ...

    def special_size(self, diameter_ordered: (int, float)):
        '''
        Проверка наличия специального заказа на диаметр пиццы более 30 см
        :param diameter_ordered: диаметр, который заказывает покупатель
        Пример:
        diameter_ordered = diameter(45)
        diameter_ordered.special_size(31)
        :return: True / False
        '''
        ...