from RestaurantManagementApp.controller.controller import Controller
from RestaurantManagementApp.repository.cooked_dish_repo import CookedDishRepo
from RestaurantManagementApp.repository.customer_repo import CustomerRepo
from RestaurantManagementApp.repository.drink_repo import DrinkRepo
from RestaurantManagementApp.repository.order_repo import OrderRepo
from RestaurantManagementApp.ui.console import Console

controller = Controller(
    CookedDishRepo("cooked_dishes.json"),
    DrinkRepo("drinks.json"),
    CustomerRepo("customers.json"),
    OrderRepo("orders.json")
)

console = Console(controller)
console.run()