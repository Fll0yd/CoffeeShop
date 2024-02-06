import tkinter as tk
from tkinter import messagebox, PhotoImage, ttk
from datetime import datetime, timedelta

class CoffeeShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flloyd's Coffee Shop")
        self.root.geometry("1500x900")  # Adjust the window size as needed

        self.font_style = ("Arial", 12)
        self.bg_color = "#22CE83"

        self.bg_image = PhotoImage(file="F:/Code/Python/Coffee/background.png")
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label_greeting = tk.Label(self.root, text="Welcome to Flloyd's Coffee! What's your name?", font=self.font_style, bg=self.bg_color)
        self.label_greeting.pack()

        self.entry_name = tk.Entry(self.root, font=self.font_style)
        self.entry_name.pack()

        # Bind the check_customer_status method to the entry widget
        self.entry_name.bind("<Return>", lambda event: self.check_customer_status())
        
        self.label_menu = tk.Label(self.root, text="What can we get started for you today?:", font=self.font_style, bg=self.bg_color)
        self.label_menu.pack()

        self.selected_items = []
        self.quantity_entries = []

        self.initial_dropdown = ttk.Combobox(self.root, values=list(PRICES.keys()), state="readonly")
        self.initial_dropdown.pack()
        self.selected_items.append(self.initial_dropdown)

        self.initial_quantity_entry = tk.Entry(self.root, font=self.font_style)
        self.initial_quantity_entry.pack()
        self.quantity_entries.append((self.initial_dropdown, self.initial_quantity_entry))

        self.label_quantity = tk.Label(self.root, text="How many of those would you like?", font=self.font_style, bg=self.bg_color)
        self.label_quantity.pack()

        self.submit_order_button = tk.Button(self.root, text="Submit Order", command=self.process_order)
        self.submit_order_button.pack()

        self.label_greeting.place(relx=0.5, rely=0.370, anchor=tk.CENTER)
        self.entry_name.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.label_menu.place(relx=0.5, rely=0.510, anchor=tk.CENTER)
        self.initial_dropdown.place(relx=0.5, rely=0.540, anchor=tk.CENTER)
        self.label_quantity.place(relx=0.5, rely=0.610, anchor=tk.CENTER)
        self.initial_quantity_entry.place(relx=0.5, rely=0.640, anchor=tk.CENTER)
        self.submit_order_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        
        self.countdown_label = tk.Label(self.root, text="", font=self.font_style, bg=self.bg_color)
        self.countdown_label.place(relx=0.85, rely=0.05, anchor=tk.CENTER)
        self.add_item_button = tk.Button(self.root, text="Add Item", command=self.add_another_item)
        self.add_item_button.pack()
        self.additional_items = []

    def check_customer_status(self):
        customer_name = self.entry_name.get()
        evil_customers = ["Ben", "Loki", "Patricia"]

        if customer_name in evil_customers:
            evil_response = messagebox.askyesno(f"Are you evil, {customer_name}?")
            if evil_response:
                messagebox.showinfo("Permission Denied", f"You're not welcome here, {customer_name}! Get out!")
                return  # Stop further actions for "evil" customers who claim to be evil
            
            # If "evil" customer claims not to be evil, proceed to ask about good deeds
            self.ask_good_deeds(customer_name)
        else:
            messagebox.showinfo("Welcome", f"Hi, {customer_name}! Thank you for visiting Flloyd's Coffee!")

    def ask_good_deeds(self, customer_name):
        good_deeds_window = tk.Toplevel(self.root)
        good_deeds_window.title("Good Deeds")
    
        label = tk.Label(good_deeds_window, text=f"How many good deeds have you done today, {customer_name}?")
        label.pack()
    
        good_deeds_entry = tk.Entry(good_deeds_window)
        good_deeds_entry.pack()
    
        confirm_button = tk.Button(good_deeds_window, text="Confirm", command=lambda: self.process_good_deeds(customer_name, good_deeds_entry))
        confirm_button.pack()

    def process_good_deeds(self, customer_name, entry):
        try:
            good_deeds = int(entry.get())
            if good_deeds > 3:
                messagebox.showinfo("Permission Granted", f"Oh!, So you're one of those rare good {customer_name}'s? Well, come on in then!")
            else:
                messagebox.showinfo("Permission Denied", f"You're not welcome here, {customer_name}! Get out!")
        except ValueError:
            messagebox.showerror("Error", "Go do more!, you evil bastard!")

    def validate_quantity(self, quantity):
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Quantity should be a positive whole number.")
            return quantity
        except ValueError:
            raise ValueError("Invalid quantity entered. Please enter a positive whole number for quantity.")

    def start_countdown(self, total_minutes):
        total_seconds = total_minutes * 60  # Convert minutes to seconds
        current_time = datetime.now()
        end_time = current_time + timedelta(seconds=total_seconds)
        self.update_countdown(end_time)

    def confirm_order(self):
        selected_items = [dropdown.get() for dropdown, _ in self.quantity_entries if dropdown.get()]
        quantities = [entry.get() for _, entry in self.quantity_entries]

        # Ensure both selected items and their corresponding quantities are available
        if not all(selected_items) or not all(quantities):
            raise ValueError("No items selected or quantity not specified for selected items.")

        quantities = [int(quantity) if quantity else 0 for quantity in quantities]  # Convert empty strings to 0

        total_cost = sum(PRICES[item] * quantity for item, quantity in zip(selected_items, quantities))
        total_items = sum(quantities)  # Sum up all quantities for selected items
        preparation_time = 5 * total_items
        preparation_time_str = f"{preparation_time} minute(s)"

        # Display and confirm the order
        confirmation = messagebox.askyesno(
            "Confirmation", f"Confirm order of {total_items} items for ${total_cost}?\n"
                            f"Estimated preparation time: {preparation_time_str}\n"
                            f"Proceed with the order?")

        # Process the order if confirmed
        if confirmation:
            total_preparation_time_seconds = preparation_time * 60
            self.start_countdown(total_preparation_time_seconds)
            self.root.after(total_preparation_time_seconds * 1000, lambda: messagebox.showinfo(
                "Order Placed", f"Your order has been placed. Total cost: ${total_cost}.\n"
                                f"Your order will be ready in {preparation_time_str}."))

        return confirmation, total_cost
        
    def update_countdown(self, end_time):
        current_time = datetime.now()
        remaining_time = end_time - current_time

        if remaining_time.total_seconds() <= 0:
            self.countdown_label.config(text="Order Up!")
        else:
            remaining_minutes = remaining_time.total_seconds() // 60
            remaining_seconds = remaining_time.total_seconds() % 60
            time_str = f"{int(remaining_minutes):02d}:{int(remaining_seconds):02d}"
            self.countdown_label.config(text=f"Order ready in: {time_str}")
            self.root.after(1000, self.update_countdown, end_time)

    def validate_order(self):
        selected_items = [dropdown.get() for dropdown in self.selected_items if dropdown.get()]
        quantities = [entry.get() for entry in self.quantity_entries]

        # Ensure both selected items and their corresponding quantities are available
        if not all(selected_items) or not all(quantities):
            messagebox.showerror("Error", "No items selected or quantity not specified for selected items.")
            return None  # Return None if validation fails

        try:
            quantities = [int(quantity) if quantity else 0 for quantity in quantities]  # Convert empty strings to 0

            total_cost = sum(PRICES[item] * quantity for item, quantity in zip(selected_items, quantities))
            preparation_time = 5 * sum(quantities)
            preparation_time_str = f"{preparation_time} minute(s)"

            return total_cost, preparation_time_str
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity entered. Please enter a positive whole number for quantity.")
            return None  # Return None if validation fails

    # Define the add_another_item method inside the class
    def add_another_item(self):
        new_dropdown = ttk.Combobox(self.root, values=list(PRICES.keys()), state="readonly")
        new_dropdown.pack()

        new_quantity_entry = tk.Entry(self.root, font=self.font_style)
        new_quantity_entry.pack()

        self.additional_items.append((new_dropdown, new_quantity_entry))

    # Modify the process_order method to include additional items
    def process_order(self):
        selected_items = [dropdown.get() for dropdown, _ in self.quantity_entries + self.additional_items if dropdown.get()]
        quantities = [entry.get() for _, entry in self.quantity_entries + self.additional_items]

        if not all(selected_items) or not all(quantities):
            messagebox.showerror("Error", "No items selected or quantity not specified for selected items.")
            return

        try:
            quantities = [int(quantity) if quantity else 0 for quantity in quantities]

            total_cost = sum(PRICES[item] * quantity for item, quantity in zip(selected_items, quantities))
            total_items = sum(quantities)
            preparation_time = 5 * total_items
            preparation_time_str = f"{preparation_time} minute(s)"

            confirmation = messagebox.askyesno(
                "Confirmation", f"Confirm order of {total_items} items for ${total_cost}?\n"
                                f"Estimated preparation time: {preparation_time_str}\n"
                                f"Proceed with the order?")

            if confirmation:
                total_preparation_time_seconds = preparation_time * 60
                self.start_countdown(total_preparation_time_seconds)
                self.root.after(total_preparation_time_seconds * 1000, lambda: messagebox.showinfo(
                    "Order Placed", f"Your order has been placed. Total cost: ${total_cost}.\n"
                                    f"Your order will be ready in {preparation_time_str}."))

        except ValueError:
            messagebox.showerror("Error", "Invalid quantity entered. Please enter a positive whole number for quantity.")

if __name__ == "__main__":
    PRICES = {
        "Espresso": 5,
        "Americano": 6,
        "Latte": 9,
        "Cappuccino": 10,
        "Mocha Coffee": 7,
        "Almond Cappuccino": 11,
        "Mint Latte": 8,
        "Coffee Frappe": 13,
        "Iced Coffee": 4,
        "Black Coffee": 3
    }

    root = tk.Tk()
    coffee_shop_app = CoffeeShopApp(root)
    root.mainloop()
