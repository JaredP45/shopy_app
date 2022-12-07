'''
File Name: hw5_starter.py
Started By: Emily Alfs-Votipka
Completed By: Jared Paubel
Section: CIS115 - 19C
Description: Basic online shopping application.
'''

def price_check(item:str, inventory:dict) -> float:
    """ Returns price of selected item """
    for product,detail in inventory.items():
        if item == product:
            return "${:.2f}".format(detail["price"])
    return -1.0

def checkout(cart:dict, inventory:dict) -> str:
    """ Returns receipt of purchases """
    total = 0.0
    receipt = ""
    # Lambda function for calcuating and formating reciept item
    item_summary = lambda item, quantity, price: "{} {} at ${:.2f}.....${:.2f}\n".format(
        quantity,
        item,
        price,
        (float(quantity)*price),
    )

    for item,detail in cart.items():
        receipt += item_summary(item, detail["quantity"], inventory[item]["price"])
        total += (detail["quantity"] * inventory[item]["price"])
    receipt += "Your total is ${:.2f}.\nThank you for shopping with us!".format(total)
    return receipt

def show_qty(inventory:dict) -> None:
    """ Prints the quantity of each item in cart """
    print("Here is our current inventory:")
    for item,detail in inventory.items():
        if detail["quantity"] > 0:
            print("\t{} of {}".format(detail["quantity"], item))
        else:
            print("\t{}: out of stock.".format(item))

def show_prices(inventory:dict) -> None:
    """ Prints the price of each item in cart """
    print("Here are our current prices:")
    for item,detail in inventory.items():
        print("\t{}.....${:.2f}".format(item, detail["price"]))

def show_cart(cart:dict) -> None:
    """ Prints the name and quantity of each item in the cart """
    if cart == {}:
        print("There is nothing in your cart...")
    else:
        print("Here is your current cart:")
        for item,detail in cart.items():
            print("\t{}.....{}".format(item, detail["quantity"]))

def add_to_cart(product:str, cart:dict, inventory:dict) -> bool:
    """ Returns boolean value indicating whether item was added to the cart """
    if product in inventory.keys() and inventory[product]["quantity"] > 0:
        if product not in cart.keys():
            cart[product] = {"quantity": 1}
        else:
            cart[product]["quantity"] += 1
        inventory[product]["quantity"] -= 1
        return True
    else:
        return False

def remove_from_cart(product:str, cart:dict, inventory:dict) -> bool:
    """ Returns boolean value indicating whether item was removed from the cart """
    if product in cart.keys() and cart[product]["quantity"] > 0:
        inventory[product]["quantity"] += 1
        cart[product]["quantity"] -= 1
        if cart[product]["quantity"] == 0:
            del cart[product]
        return True
    else:
        return False

def main():
    """
    The primary logic of this small shopping program
    """
    inventory = {
        'Eggs': {'quantity': 7, 'price': 2.07},
        'Milk': {'quantity': 5, 'price': 3.42},
        'Cheese': {'quantity': 4, 'price': 4.98},
        'Bread': {'quantity': 7, 'price': 2.72},
        'Ketchup': {'quantity': 5, 'price': 3.98},
        'Mustard': {'quantity': 2, 'price': 2.72},
        'Turkey': {'quantity': 3, 'price': 34.58},
        'Chicken': {'quantity': 4, 'price': 14.92}
    }
    cart = {}
    shopping = True

    print("Welcome to our store!")

    while shopping:
        print('''Do you want to:
        Check (P)rice
        (V)iew inventory
        (S)how cart
        (G)et item
        (R)eturn an item from your cart? or
        (C)heckout
        ''')
        userInput = input("Enter Choice: ")

        if userInput in ["P", "p"]:
            choice = str(input("What item do you want to check the price on? >> "))
            print(price_check(choice, inventory))
        elif userInput in ["V", "v"]:
            show_qty(inventory)
        elif userInput in ["S", "s"]:
            show_cart(cart)
        elif userInput in ["G", "g"]:
            choice = str(input("What item do you want to add? >> "))
            is_item_added = add_to_cart(choice, cart, inventory)
            if is_item_added:
                print("Item was added to cart")
            else:
                print("Item is not in stock")
        elif userInput in ["R", "r"]:
            choice = str(input("What item do you want to remove? >> "))
            is_item_removed = remove_from_cart(choice, cart, inventory)
            if is_item_removed:
                print("Item was removed")
            else:
                print("Item is not in your cart")
        elif userInput in ["C", "c"]:
            print(checkout(cart, inventory))
            shopping = False
main()