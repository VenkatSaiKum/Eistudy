# product.py
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available

    @abstractmethod
    def clone(self):
        pass

# Concrete product class
class ConcreteProduct(Product):
    def clone(self):
        return ConcreteProduct(self.name, self.price, self.available)

# discount_strategy.py
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

# Concrete discount strategy class
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)

# cart.py
class ShoppingCart:
    def __init__(self, discount_strategy=None):
        self.cart_items = {}
        self.discount_strategy = discount_strategy

    def add_to_cart(self, product, quantity):
        if isinstance(product, Product) and product.available and quantity > 0:
            if product.name in self.cart_items:
                self.cart_items[product.name]["quantity"] += quantity
            else:
                self.cart_items[product.name] = {"product": product, "quantity": quantity}

    def update_quantity(self, product, quantity):
        if product.name in self.cart_items and quantity > 0:
            self.cart_items[product.name]["quantity"] = quantity

    def remove_from_cart(self, product):
        if product.name in self.cart_items:
            del self.cart_items[product.name]

    def calculate_total_bill(self):
        total_price = sum(item["product"].price * item["quantity"] for item in self.cart_items.values())
        if self.discount_strategy:
            total_price = self.discount_strategy.apply_discount(total_price)
        return total_price

# main.py
if __name__ == "__main__":
    laptop = ConcreteProduct("Laptop", 1000, True)
    headphones = ConcreteProduct("Headphones", 50, True)

    percentage_discount = PercentageDiscount(0.1)  # 10% discount

    cart = ShoppingCart(percentage_discount)

    while True:
        print("Available Products:")
        print(f"1. {laptop.name} - ${laptop.price} ({'Available' if laptop.available else 'Not Available'})")
        print(f"2. {headphones.name} - ${headphones.price} ({'Available' if headphones.available else 'Not Available'})")
        print("3. View Cart")
        print("4. Checkout and Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            quantity = int(input(f"How many {laptop.name}s do you want to add to the cart? "))
            cart.add_to_cart(laptop, quantity)
        elif choice == "2":
            quantity = int(input(f"How many {headphones.name}s do you want to add to the cart? "))
            cart.add_to_cart(headphones, quantity)
        elif choice == "3":
            print(f"Cart Items: {cart.cart_items}")
            print(f"Total Bill: Your total bill is ${cart.calculate_total_bill()}.")
        elif choice == "4":
            print("You have " , cart.cart_items["Laptop"]["quantity"] , " Laptops and you have " , cart.cart_items["Headphones"]["quantity"] , " Headphones.")
            print(f" Your total bill is ${cart.calculate_total_bill()}.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
