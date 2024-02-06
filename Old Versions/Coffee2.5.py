print("Hello, welcome to Flloyd's Coffee!")

name = input("What's your name?\n")

if name in ["Ben", "Loki", "Patricia"]:
    while True:
        evil_status = input("Are you evil?\n")
        if evil_status.lower() == "yes":
            print(f"You're not welcome here {name}!! Get out!!")
            exit()
        elif evil_status.lower() == "no":
            print(f"Oh!, So you're one of those rare good {name}'s? Well come on in then!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

else:
    print(f"Hello {name}, thank you so much for coming in today.\n")

menu = "Black Coffee \nEspresso \nLatte \nCappuccino \nFrappuccino \n"

def get_order(menu):
    while True:
        order = input(f"Here is what we are currently serving:\n{menu}What can I get started for you?\n")
        if order.lower() in ["frappuccino", "black coffee", "espresso", "latte", "cappuccino"]:
            return order.lower()
        else:
            print(f"Sorry, we don't currently offer {order} at this time.")

order = get_order(menu)

prices = {"frappuccino": 13, "black coffee": 3, "espresso": 5, "latte": 9, "cappuccino": 10}

price = prices[order]

quantity = input(f"And how many of those {order}'s would you like?\n")

try:
    total = price * int(quantity)
    print(f"Your order today comes to ${total}.")
except ValueError:
    print("Invalid quantity entered. Please enter a valid integer value for quantity.")

exit()
