# This program will attempt to be a mini database and have GUI for the user
# This program was made by Harris Domangue on Nov 26th 2024 for CMSC-201 at 9:33pm

import tkinter as tk

# Items for sale
Computerstuff = {"Keyboards": 7.99, "Mice": 5.99, "Keyboard and Mice": 11.99}

# Databases
DataBaseName = {}  # ID -> Name
DataBasePurchase = {}  # ID -> Item Purchased

# Functions
def add_customer():
    try:
        name = name_entry.get()  # Get the customer's name from the GUI entry field.
        customer_id = int(id_entry.get())  # Get the customer's ID, converting it to an integer.
        item = item_var.get()  # Get the item purchased from the dropdown menu.

        # Validation: Check if all fields are filled out
        if not name or not item:
            error_label.config(text="Error: All fields must be filled out!", fg="red")  # Display error.
            return  # Exit the function if validation fails.

        # Add the customer's data to the databases
        DataBaseName[customer_id] = name  # Store the name in the `DataBaseName` dictionary with ID as the key.
        DataBasePurchase[customer_id] = item  # Store the purchased item in the `DataBasePurchase` dictionary with ID as the key.

        # Success Message
        error_label.config(text="Success: Customer added successfully!", fg="green")  # Display success.

        # Clear the input fields for the next entry
        name_entry.delete(0, tk.END)  # Clear the name entry field.
        id_entry.delete(0, tk.END)  # Clear the ID entry field.

    except ValueError:  # Handle the case where ID is not a number
        error_label.config(text="Error: Customer ID must be a number!", fg="red")  # Display error.

def search_customer():
    try:
        customer_id = int(id_entry.get())

        name = DataBaseName[customer_id]
        item = DataBasePurchase[customer_id]

        # Success Message
        error_label.config(
            text=f"Success: Found Customer ID {customer_id}!\nName: {name}, Item: {item}",
            fg="green"
        )
    except KeyError:
        error_label.config(text="Error: Customer ID not found!", fg="red")
    except ValueError:
        error_label.config(text="Error: Customer ID must be a number!", fg="red")

def delete_customer():
    try:
        customer_id = int(id_entry.get())

        if customer_id in DataBaseName:
            del DataBaseName[customer_id]
            del DataBasePurchase[customer_id]
            error_label.config(text="Success: Customer deleted successfully!", fg="green")
        else:
            raise KeyError

    except KeyError:
        error_label.config(text="Error: Customer ID not found!", fg="red")
    except ValueError:
        error_label.config(text="Error: Customer ID must be a number!", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Computer Supplies Database")

# Input Fields
tk.Label(root, text="Customer Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Customer ID:").grid(row=1, column=0, padx=5, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Item Purchased:").grid(row=2, column=0, padx=5, pady=5)
item_var = tk.StringVar(value="Keyboards")
item_menu = tk.OptionMenu(root, item_var, *Computerstuff.keys())
item_menu.grid(row=2, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Customer", command=add_customer)
add_button.grid(row=3, column=0, padx=5, pady=5)

search_button = tk.Button(root, text="Search Customer", command=search_customer)
search_button.grid(row=3, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Customer", command=delete_customer)
delete_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Error/Success Label
error_label = tk.Label(root, text="", fg="red")  # Default is empty with red text.
error_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Start GUI Loop
root.mainloop()
