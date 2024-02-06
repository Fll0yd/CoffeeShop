def get_validated_input(prompt, valid_options=None):
    # Prompt user for input and validate against valid options.
    while True:
        user_input = input(prompt).strip().lower()
        if valid_options and user_input not in valid_options:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")
        else:
            return user_input

def check_customer_status(name):
    # Check if the customer is listed as 'evil' or 'good'.
    evil_statuses = {
        "Ben": False,
        "Loki": False,
        "Patricia": False
    }
    if name in evil_statuses:
        return get_validated_input("Are you evil?\n", ["yes", "no"])
    else:
        print(f"Hello {name}, thank you so much for coming in today.")
        return "no"  # Defaulting to "no" for non-listed names

def calculate_total_price(price, quantity):
    # Calculate the total cost based on price and quantity.
    try:
        return price * int(quantity)
    except ValueError:
        print("Invalid quantity entered. Please enter a valid integer value for quantity.")
        return None

def main():
    print("Hello, welcome to Flloyd's Coffee!")
    customer_name = get_validated_input("What's your name?\n").capitalize()
    
    customer_status = check_customer_status(customer_name)
    
    if customer_status == "yes":
        print(f"You're not welcome here, {customer_name}! Get out!")
        exit()
    elif customer_status == "no":
        print(f"Oh!, So you're one of those rare good {customer_name}'s? Well, come on in then!")

    MENU = ["black coffee", "espresso", "latte", "cappuccino", "frappuccino"]
    menu_str = "\n".join(MENU).capitalize()
    
    ordered_item = get_validated_input(f"Here is what we are currently serving:\n{menu_str}\nWhat can I get started for you?\n", MENU)
    
    PRICES = {
        "frappuccino": 13, 
        "black coffee": 3, 
        "espresso": 5, 
        "latte": 9, 
        "cappuccino": 10
    }
    
    item_price = PRICES[ordered_item]
    ordered_quantity = get_validated_input(f"And how many of those {ordered_item}'s would you like?\n")
    
    total_cost = calculate_total_price(item_price, ordered_quantity)
    if total_cost is not None:
        print(f"Your order today comes to ${total_cost}.")

if __name__ == '__main__':
    main()
