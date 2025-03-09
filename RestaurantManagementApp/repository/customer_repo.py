from RestaurantManagementApp.repository.data_repo import DataRepo
from RestaurantManagementApp.model.customer import Customer


def convert_dictionary_to_customer(dictionary_from_json):
    customer = Customer(
        id=dictionary_from_json.get("id", -1),
        name=dictionary_from_json.get("name", "UNKNOWN"),
        address=dictionary_from_json.get("address", "UNKNOWN")
    )
    return customer


def convert_customer_to_dictionary(customer):
    return {
        "id": customer.id,
        "name": customer.name,
        "address": customer.address
    }


class CustomerRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)
        self.read_file()

    def convert_to_string(self, object_list) -> list:
        return list(map(convert_customer_to_dictionary, self.get_all()))

    def convert_from_string(self, dictionary_list_from_json) -> list:
        customers = list(map(convert_dictionary_to_customer, dictionary_list_from_json))
        return customers

    def find_by_name(self, name):
        return list(filter(lambda customer: name.lower() in customer.name.lower(), self.get_all()))

    def find_by_address(self, address):
        return list(filter(lambda customer: address.lower() in customer.address.lower(), self.get_all()))
