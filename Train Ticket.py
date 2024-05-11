import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def print_ticket():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    if gender == 'M':
        gender_str = 'Male'
    elif gender == 'F':
        gender_str = 'Female'

    ticket_class = class_var.get()
    if ticket_class == 'First Class':
        ticket_price = 100
    elif ticket_class == 'Second Class':
        ticket_price = 50

    ticket_info = f'Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\nName: {name}\nAge: {age}\nGender: {gender_str}\nTicket Class: {ticket_class}\nTicket Price: {ticket_price} pounds'

    messagebox.showinfo("Train Ticket", ticket_info)

root = tk.Tk()
root.title("Train Ticket Program")

# Labels
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5)
gender_label = tk.Label(root, text="Gender (M/F):")
gender_label.grid(row=2, column=0, padx=10, pady=5)
class_label = tk.Label(root, text="Ticket Class:")
class_label.grid(row=3, column=0, padx=10, pady=5)

# Entries
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

# Radio Buttons for Gender
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value='M')
male_radio.grid(row=2, column=1, padx=10, pady=5)
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value='F')
female_radio.grid(row=2, column=2, padx=10, pady=5)

# Radio Buttons for Ticket Class
class_var = tk.StringVar()
first_class_radio = tk.Radiobutton(root, text="First Class", variable=class_var, value='First Class')
first_class_radio.grid(row=3, column=1, padx=10, pady=5)
second_class_radio = tk.Radiobutton(root, text="Second Class", variable=class_var, value='Second Class')
second_class_radio.grid(row=3, column=2, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Print Ticket", command=print_ticket)
submit_button.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
