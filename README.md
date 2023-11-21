# Eistudy

# Simple E-commerce Cart System This is a simple E-commerce cart system implemented in Python. The system allows users to add products to their cart, update quantities, and view the total bill. It also incorporates design patterns like the Strategy Pattern for handling different discount strategies and the Prototype Pattern for cloning product objects. 

## File Structure - 
**product.py:** Defines the base Product class and a concrete implementation, ConcreteProduct. -
**discount_strategy.py:** Implements the DiscountStrategy interface and provides a concrete strategy, PercentageDiscount. - 
**cart.py:** Contains the ShoppingCart class, which manages the cart items, allows updating quantities, and calculates the total bill. It uses the Prototype Pattern to clone product objects when adding them to the cart. - 
**main.py:** The main executable file where users can interact with the system through a simple console-based interface. It demonstrates how to create products, add them to the cart, and calculate the total bill with a discount strategy.
## Usage 1. Run `main.py` to start the program. 
2. Choose options to add products, view the cart, and checkout. ##
