import json
import hashlib
import os
from multiprocessing import Pool


class NewElemnt:


    def new_element(marka=None, model=None, year=None, engine=None, color=None, kuzov=None, mileage=None, price=None):
        print()
        """принимает аргументы в таком порядке:
        марка,модель, год,цвет,тип кузова, километраж,цена"""
        new = {"марка машины": marka, "модель машины": model, 'дата выпуска': year,
               'объем двигателя': engine, "цвет машины": color,
               "тип кузова": kuzov, "километраж": mileage, "цена": price, }
        return new


class CreateMixin:
    def create(self, new_element):
        self.list_.append(new_element)


class ListingMixin:
    def listing(self):
        print(f"Вот ваш список - {self.list_}")


class RetrieveMixin:
    def retrieve(self):
        import random
        random_element = random.choice(self.list_)
        print(f"Один элемент из списка - {random_element}")
        return ''


class UpdateMixin:
    def update(self, change_element_index, new_lement):
        try:
            self.list_[change_element_index] = new_lement
            print(f"Вот обновленный список - {self.list_}")
            return ''
        except IndexError:
            print("Такого элемента в списке не найдено!")
            return ''


class DeleteMixin:
    def delete(self, what_delete_index):
        if what_delete_index.lower() == "all" or what_delete_index == "все":
            self.list_.clear()
            print("Список поностью очищен !")
            return ""
        try:
            del self.list_[what_delete_index]
            print(f"Элемент был удален!")
            return ''
        except IndexError:
            print("Такого элемента нет!")
            return ""


class Cars(CreateMixin, ListingMixin, DeleteMixin, UpdateMixin, RetrieveMixin,NewElemnt):
    def __init__(self, marka=None, model=None, year_of_start=None, engine_capacity=None, color=None, body_type=None,
                 mileage=None, price=None, lilol=None):
        self.marka = marka
        self.model = model
        self.year_of_start = year_of_start
        self.engine_capacity = engine_capacity
        self.color = color
        self.body_type = body_type
        self.mileage = mileage
        self.price = price
        self.lilol = lilol

    list_ = []

    def prepareforjson(self):
        our_dict = {"марка машины": self.marka, "модель машины": self.model, 'дата выпуска': self.year_of_start,
                    'объем двигателя': self.engine_capacity, "цвет машины": self.color,
                    "тип кузова": self.body_type, "километраж": self.mileage, "цена": self.price, 'ссылка': self.lilol}
        self.list_.append(our_dict)

    def send_to_json(self):
        with open("database.json", "w") as file:
            # Записываем данные в файл в формате JSON
            json.dump(self.list_, file, ensure_ascii=False, indent=4)
        # with open("database.json", "a") as file:
        #     json.dump(our_dict, file, ensure_ascii=False)
