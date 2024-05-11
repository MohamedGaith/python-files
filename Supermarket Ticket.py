import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Global variables
products = {
    "Milk": 10,
    "Bread": 5,
    "Eggs": 8,
    "Butter": 15,
    "Cheese": 20
}

def calculate_discount(total_price):
    if 100 <= total_price < 200:
        return total_price * 0.05
    elif 200 <= total_price < 300:
        return total_price * 0.1
    elif total_price >= 300:
        return total_price * 0.15
    else:
        return 0

def print_receipt():
    name = name_entry.get()
    phone = phone_entry.get()
    units = [int(entry.get()) for entry in entries]
    
    total_price = sum(units[i] * list(products.values())[i] for i in range(len(units)))
    discount = calculate_discount(total_price)
    final_price = total_price - discount
    
    # Print receipt
    receipt = f"Date: {datetime.now().strftime('%Y-%m-%d')}\nSupermarket Name: Al-manar Supermarket\nReceipt Number: 001\nCustomer Name: {name}\nPhone Number: {phone}\n\n"
    receipt += "Product\t\tUnit Price\t\tUnits\t\tTotal Price\n"
    for product, unit, price in zip(products.keys(), units, products.values()):
        receipt += f"{product}\t\t{price} pounds\t\t{unit}\t\t\t{unit * price} pounds\n"
    receipt += f"\nTotal Price Before Discount: {total_price} pounds\nDiscount: {discount} pounds\nTotal Price After Discount: {final_price} pounds"
    
    messagebox.showinfo("Supermarket Receipt", receipt)

root = tk.Tk()
root.title("Supermarket Billing Program")

# Labels
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
phone_label = tk.Label(root, text="Phone Number:")
phone_label.grid(row=1, column=0, padx=10, pady=5)

# Entries
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

# Product labels and entries
entries = []
for i, (product, price) in enumerate(products.items(), start=2):
    label = tk.Label(root, text=product)
    label.grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Print Button
print_button = tk.Button(root, text="Print Receipt", command=print_receipt)
print_button.grid(row=len(products)+2, column=0, columnspan=2, pady=10)

root.mainloop()
