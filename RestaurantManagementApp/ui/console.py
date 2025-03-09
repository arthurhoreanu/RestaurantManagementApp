from RestaurantManagementApp.controller.controller import (Controller)
from RestaurantManagementApp.model.cooked_dish import CookedDish
from RestaurantManagementApp.model.customer import Customer
from RestaurantManagementApp.model.drink import Drink
from RestaurantManagementApp.model.order import Order


def list_printer(entity_type, entity_list):
    type = entity_type.replace("_", " ").title()

    if len(entity_list) > 0:
        print("\n".join(map(lambda ordered_item: f"   {type}: {ordered_item.copy()}", entity_list)))
    else:
        print(f"   {type} list is empty")


def entity_chooser():
    choosen_entity = None
    print("1 - Cooked Dish")
    print("2 - Drink")
    print("3 - Customer")
    print("4 - Order")

    command = input(">>> ")

    if command == "1":
        choosen_entity = "cooked_dish"
    elif command == "2":
        choosen_entity = "drink"
    elif command == "3":
        choosen_entity = "customer"
    elif command == "4":
        choosen_entity = "order"

    return choosen_entity


class Console:
    def __init__(self, controller: Controller):
        self.__controller = controller

    def create_entity(self, entity_type):
        new_entity = None

        if entity_type == "cooked_dish":
            cooked_dish = CookedDish(-1, -1, -1, -1)
            cooked_dish.id = int(input("New id: "))
            cooked_dish.serving_size = int(input("New serving size: "))
            cooked_dish.price = float(input("New price: "))
            cooked_dish.preparation_time = input("New preparation time: ")
            new_entity = cooked_dish

        elif entity_type == "drink":
            drink = Drink(-1, -1, -1, -1)
            drink.id = int(input("New id: "))
            drink.serving_size = int(input("New serving size: "))
            drink.price = float(input("New price: "))
            drink.alcohol_content = int(input("New alcohol content: "))
            new_entity = drink

        elif entity_type == "customer":
            customer = Customer(-1, "", "")
            customer.id = int(input("New id: "))
            customer.name = input("New name: ")
            customer.address = input("New address: ")
            new_entity = customer

        elif entity_type == "order":
            order = Order(-1, -1, [], [])
            order.id = int(input("New id: "))
            order.customer_id = int(input("New customer id: "))
            dishes = []

            while True:
                cooked_dishes_list = self.__controller.get_all("cooked_dish")

                if len(cooked_dishes_list) < 1:
                    break

                list_printer("cooked_dish", cooked_dishes_list)

                id = int(input("What would you like to eat?: "))
                print("\n-Press -1 to exit")

                if id <= 0:
                    break
                else:
                    dishes.append(self.__controller.get_by_id(id, "cooked_dish"))

            order.dishes = dishes

            drinks = []

            while True:
                drinks_list = self.__controller.get_all("drink")

                if len(drinks_list) < 1:
                    break

                list_printer("drink", drinks_list)

                id = int(input("What would you like to drink?: "))
                print("\n-Press -1 to exit")

                if id <= 0:
                    break
                else:
                    drinks.append(self.__controller.get_by_id(id, "drink"))

            order.drinks = drinks

            new_entity = order

        return new_entity

    def print_menu(self):
        print("Current items:")
        print(f"Cooked dishes: {[cooked_dish.copy() for cooked_dish in self.__controller.get_all('cooked_dish')]}")
        print(f"Drinks: {[drink.copy() for drink in self.__controller.get_all('drink')]}")
        print(f"Customers: {[drink.copy() for drink in self.__controller.get_all('customer')]}")
        print(f"Orders: {[drink.copy() for drink in self.__controller.get_all('order')]}")

        print("\nMain Menu: ")
        print("0 - Exit")
        print("1 - Add")
        print("2 - Display items")
        print("3 - Find customer by name")
        print("4 - Find customer by address")
        print("5 - Generate invoice")
        print("6 - Update")
        print("7 - Delete")
        print("8 - Menu")
        print("9 - Get item by ID")

    def run(self):
        self.__controller.read_file("cooked_dishes.json")
        self.__controller.read_file("drinks.json")
        self.__controller.read_file("customers.json")
        self.__controller.read_file("orders.json")
        self.print_menu()

        command = input("\nChoose a command number: ")

        while command != "0":
            if command == "1":
                entity_type = entity_chooser()
                new_entity = self.create_entity(entity_type)

                self.__controller.add(new_entity, entity_type)
                print("Added successfully")
            elif command == "2":
                entity_type = entity_chooser()

                list_printer(entity_type, self.__controller.get_all(entity_type))

            elif command == "3":
                name = input("Name: ")

                list_printer("customer", self.__controller.find_customer_by_name(name))

            elif command == "4":
                address = input("Address: ")

                list_printer("customer", self.__controller.find_customer_by_address(address))

            elif command == "5":
                id = int(input("Customer id: "))

                found = None

                for order in self.__controller.get_all("order"):
                    if order.customer_id == id:
                        order.display_invoice()
                        found = order.customer_id

                if not found:
                    print("Try again")
            elif command == "6":
                entity_type = entity_chooser()

                list_printer(entity_type, self.__controller.get_all(entity_type))

                id = int(input("Update item with this id: "))

                new_entity = self.create_entity(entity_type)

                self.__controller.update_by_id(id, new_entity, entity_type)

            elif command == "7":
                entity_type = entity_chooser()
                list_printer(entity_type, self.__controller.get_all(entity_type))
                id = int(input("Delete item with this id: "))
                self.__controller.delete_by_id(id, entity_type)

            elif command == "8":
                self.print_menu()

            elif command == "9":
                entity_type = entity_chooser()
                list_printer(entity_type, self.__controller.get_all(entity_type))
                id = int(input("Get by this id: "))
                print(self.__controller.get_by_id(id, entity_type).copy())

            if command in ["3", "5", "6", "9", "10"]:
                list_printer("cooked_dish", self.__controller.get_all("cooked_dish"))
                list_printer("drink", self.__controller.get_all("drink"))
                list_printer("customer", self.__controller.get_all("customer"))
                list_printer("order", self.__controller.get_all("order"))

            command = input("\nChoose a command number: ")
