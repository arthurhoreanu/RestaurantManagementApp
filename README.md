# RestaurantManagementApp

RestaurantManagementApp is a Python-based project designed to manage restaurant operations efficiently. It allows users to handle various entities such as cooked dishes, drinks, customers, and orders through a console interface.

## Features

- **Add Entities**: Create new cooked dishes, drinks, customers, and orders.
- **Display Items**: View lists of all entities.
- **Search Customers**: Find customers by name or address.
- **Generate Invoices**: Create invoices for customer orders.
- **Update Entities**: Modify existing entities.
- **Delete Entities**: Remove entities from the system.
- **Retrieve by ID**: Fetch specific entities by their ID.

## File Structure

<pre>
📂 model (Data Models)
    identifiable.py - Defines the Identifiable abstract class
    customer.py - Defines the Customer model
    dish.py - Defines the abstract Dish model
      cooked_dish.py - Defines the CookedDish model
      drink.py - Defines the Drink model
    order.py - Defines the Order model

📂 repository (Data Repositories)
    data_repo.py - Provides a base class for data repositories
    customer_repo.py - Handles data operations for Customer entities
    cooked_dish_repo.py - Handles data operations for CookedDish entities
    drink_repo.py - Handles data operations for Drink entities
    order_repo.py - Handles data operations for Order entities

📂 controller (Business Logic)
    controller.py - Manages the business logic and interactions between models and the UI

📂 ui (User Interface)
    console.py - Contains the console interface and main application logic

📂 tests (Unit Tests)
    test.py - Contains unit tests for the application

customers.json - Stores the customers data
cooked_dishes.json - Stores the cooked dishes data
drinks.json - Stores the drinks data
orders.json - Stores the orders data

main.py - Entry point of the application
</pre>
