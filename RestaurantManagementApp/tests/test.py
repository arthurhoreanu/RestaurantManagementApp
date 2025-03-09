from RestaurantManagementApp.model.customer import Customer
from RestaurantManagementApp.model.cooked_dish import CookedDish
from RestaurantManagementApp.model.drink import Drink
from RestaurantManagementApp.model.order import Order
from RestaurantManagementApp.repository.customer_repo import CustomerRepo
from RestaurantManagementApp.repository.cooked_dish_repo import CookedDishRepo
from RestaurantManagementApp.repository.drink_repo import DrinkRepo
from RestaurantManagementApp.repository.order_repo import OrderRepo

def test_customer():
    # Initialize repository
    customer_repo = CustomerRepo("../customers.json")

    # Create
    new_customer = Customer(id=999, name="Test Customer", address="Test Address")
    customer_repo.add(new_customer)
    customer_repo.write_to_file()
    assert customer_repo.get_by_id(999) is not None

    # Read
    customer = customer_repo.get_by_id(999)
    assert customer is not None
    assert customer.name == "Test Customer"
    assert customer.address == "Test Address"

    # Update
    updated_customer = Customer(id=999, name="Updated Customer", address="Updated Address")
    customer_repo.update_by_id(999, updated_customer)
    customer_repo.write_to_file()
    customer = customer_repo.get_by_id(999)
    assert customer is not None
    assert customer.name == "Updated Customer"
    assert customer.address == "Updated Address"

    # Delete
    customer_repo.delete_by_id(999)
    customer_repo.write_to_file()

    assert customer_repo.get_by_id(999) is None

    print("All tests for customer passed.")

def test_cooked_dish():
    # Initialize repository
    cooked_dish_repo = CookedDishRepo("../cooked_dishes.json")

    # Create
    new_dish = CookedDish(id=999, serving_size=2, price=10.0, preparation_time=15)
    cooked_dish_repo.add(new_dish)
    cooked_dish_repo.write_to_file()
    assert cooked_dish_repo.get_by_id(999) is not None

    # Read
    dish = cooked_dish_repo.get_by_id(999)
    assert dish is not None
    assert dish.serving_size == 2
    assert dish.price == 10.0
    assert dish.preparation_time == 15

    # Update
    updated_dish = CookedDish(id=999, serving_size=3, price=12.0, preparation_time=20)
    cooked_dish_repo.update_by_id(999, updated_dish)
    cooked_dish_repo.write_to_file()
    dish = cooked_dish_repo.get_by_id(999)
    assert dish is not None
    assert dish.serving_size == 3
    assert dish.price == 12.0
    assert dish.preparation_time == 20

    # Delete
    cooked_dish_repo.delete_by_id(999)
    cooked_dish_repo.write_to_file()
    assert cooked_dish_repo.get_by_id(999) is None

    print("All tests for cooked dish passed.")

def test_drink():
    # Initialize repository
    drink_repo = DrinkRepo("../drinks.json")

    # Create
    new_drink = Drink(id=999, serving_size=500, price=5.0, alcohol_content=5.0)
    drink_repo.add(new_drink)
    drink_repo.write_to_file()
    assert drink_repo.get_by_id(999) is not None

    # Read
    drink = drink_repo.get_by_id(999)
    assert drink is not None
    assert drink.serving_size == 500
    assert drink.price == 5.0
    assert drink.alcohol_content == 5.0

    # Update
    updated_drink = Drink(id=999, serving_size=750, price=7.0, alcohol_content=7.0)
    drink_repo.update_by_id(999, updated_drink)
    drink_repo.write_to_file()
    drink = drink_repo.get_by_id(999)
    assert drink is not None
    assert drink.serving_size == 750
    assert drink.price == 7.0
    assert drink.alcohol_content == 7.0

    # Delete
    drink_repo.delete_by_id(999)
    drink_repo.write_to_file()
    assert drink_repo.get_by_id(999) is None

    print("All tests for drink passed.")

def test_order():
    # Initialize repository
    order_repo = OrderRepo("../orders.json")

    # Create
    new_order = Order(id=999, customer_id=1, dishes=[], drinks=[])
    order_repo.add(new_order)
    order_repo.write_to_file()
    assert order_repo.get_by_id(999) is not None

    # Read
    order = order_repo.get_by_id(999)
    assert order is not None
    assert order.customer_id == 1
    assert order.total_cost == 0.0

    # Update
    updated_order = Order(id=999, customer_id=1, dishes=[CookedDish(1, 2, 10.0, 15)], drinks=[Drink(1, 500, 5.0, 5.0)])
    order_repo.update_by_id(999, updated_order)
    order_repo.write_to_file()
    order = order_repo.get_by_id(999)
    assert order is not None
    assert order.customer_id == 1
    assert len(order.dishes) == 1
    assert len(order.drinks) == 1
    assert order.total_cost == 15.0

    # Delete
    order_repo.delete_by_id(999)
    order_repo.write_to_file()
    assert order_repo.get_by_id(999) is None

    print("All tests for order passed.")

test_customer()
test_cooked_dish()
test_drink()
test_order()