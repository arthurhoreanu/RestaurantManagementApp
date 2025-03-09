from RestaurantManagementApp.repository.data_repo import DataRepo
from RestaurantManagementApp.model.cooked_dish import CookedDish


def convert_dictionary_to_cooked_dish(dictionary_from_json):
    cooked_dish = CookedDish(-1, -1, -1, -1)
    cooked_dish.id = dictionary_from_json["id"]
    cooked_dish.serving_size = dictionary_from_json["serving_size"]
    cooked_dish.price = dictionary_from_json["price"]
    cooked_dish.preparation_time = dictionary_from_json["preparation_time"]
    return cooked_dish


def convert_cooked_dish_to_dictionary(cooked_dish):
    return {
        "id": cooked_dish.id,
        "serving_size": cooked_dish.serving_size,
        "price": cooked_dish.price,
        "preparation_time": cooked_dish.preparation_time
    }


class CookedDishRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)
        self.read_file()

    def convert_to_string(self, object_list) -> list:
        return list(map(convert_cooked_dish_to_dictionary, object_list))

    def convert_from_string(self, dictionary_list_from_json) -> list:
        return list(map(convert_dictionary_to_cooked_dish, dictionary_list_from_json))
