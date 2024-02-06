def is_customer_welcome(name):
    if name in ["Ben", "Patricia", "Loki"]:
        evil_status = input("Are you evil?\n")
        good_deeds = int(input("How many good deeds have you done today?\n"))
        if evil_status == "Yes" and good_deeds < 4:
            print(f"You're not welcome here, evil {name}!! Get out!!")
            return False
        else:
            print(f"Oh, so you're one of those rare good {name}s? Well, in that case, come on in!")
            return True
    else:
        print(f"Hello {name}, thank you so much for coming in today.")
        return True


def get_coffee_price(coffee_name):
    coffee_prices = {"black coffee": 3, "espresso": 5, "latte": 9, "cappuccino": 10, "frappuccino": 13}
    try:
        return coffee_prices[coffee_name.lower()]
    except KeyError:
        print(f"Sorry, we do not currently offer {coffee_name} at this time.")
        return 0


def calculate_total_cost(price, quantity):
    try:
        quantity = int(quantity)
    except ValueError:
        print("Invalid input for quantity. Please enter a valid integer.")
        return 0
    total = price * quantity
    return total


print("Hello, welcome to Flloyd's Coffee!")
customer_name = input("What's your name?\n")
if not is_customer_welcome(customer_name):
    exit()

coffee_name = input("Here is what we are currently serving:\nBlack Coffee\nEspresso\nLatte\nCappuccino\nFrappuccino\n\nWhat can I get started for you?\n")
coffee_price = get_coffee_price(coffee_name)

if not coffee_price:
    exit()

quantity = input(f"And how many {coffee_name}s would you like?\n")
total_cost = calculate_total_cost(coffee_price, quantity)

if not total_cost:
    exit()

print(f"{quantity} {coffee_name}s? Perfect! Coming right up, {customer_name}!")
print(f"Your order today comes to ${total_cost}. Thank you for visiting Flloyd's Coffee!")
