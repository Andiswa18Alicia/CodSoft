import tkinter as tk
from tkinter import ttk
import re 

contacts = {}

def add_contact():
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not re.match(r'^0\d{9}$', phone_number):
        status_label["text"] = "Invalid phone number format. It should start with 0 and be 10 digits long."
        return

    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        status_label["text"] = "Invalid email address."
        return

    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    update_contact_list()
    clear_entries()
    status_label["text"] = f"{name} added to contacts."

def search_contact():
    query = search_entry.get()
    results = []
    for name, info in contacts.items():
        if query.lower() in name.lower() or query in info['phone_number']:
            results.append((name, info))

    if not results:
        status_label["text"] = "No matching contacts found."
    else:
        status_label["text"] = "Matching Contacts:"
        contact_tree.delete(*contact_tree.get_children())
        for name, info in results:
            contact_tree.insert('', 'end', values=(name, info['phone_number'], info['email'], info['address']))

def update_contact():
    selected_item = contact_tree.selection()
    if selected_item:
        contact_name = contact_tree.item(selected_item, 'values')[0]
        phone_number = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        
        if not re.match(r'^0\d{9}$', phone_number):
            status_label["text"] = "Invalid phone number format. It should start with 0 and be 10 digits long."
            return

        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            status_label["text"] = "Invalid email address."
            return

        contacts[contact_name] = {
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        update_contact_list()
        clear_entries()
        status_label["text"] = f"{contact_name}'s contact information updated."
    else:
        status_label["text"] = "No contact selected for update."

def clear_entries():
    name_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    address_entry.delete(0, 'end')

def delete_selected_contact():
    selected_item = contact_tree.selection()
    if selected_item:
        contact_name = contact_tree.item(selected_item, 'values')[0]
        del contacts[contact_name]
        update_contact_list()
        status_label["text"] = f"{contact_name}'s contact deleted."
    else:
        status_label["text"] = "No contact selected for deletion."

def update_contact_list():
    contact_tree.delete(*contact_tree.get_children())
    for name, info in contacts.items():
        contact_tree.insert('', 'end', values=(name, info['phone_number'], info['email'], info['address']))


root = tk.Tk()
root.title("Contact Book")


frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

name_label = ttk.Label(frame, text="Name:")
name_entry = ttk.Entry(frame)

phone_label = ttk.Label(frame, text="Phone Number:")
phone_entry = ttk.Entry(frame)

email_label = ttk.Label(frame, text="Email:")
email_entry = ttk.Entry(frame)

address_label = ttk.Label(frame, text="Address:")
address_entry = ttk.Entry(frame)

add_button = ttk.Button(frame, text="Add Contact", command=add_contact)
update_button = ttk.Button(frame, text="Update Contact", command=update_contact)
delete_button = ttk.Button(frame, text="Delete Contact", command=delete_selected_contact)

contact_tree = ttk.Treeview(frame, columns=('Name', 'Phone Number', 'Email', 'Address'), show='headings')
contact_tree.heading('Name', text='Name')
contact_tree.heading('Phone Number', text='Phone Number')
contact_tree.heading('Email', text='Email')
contact_tree.heading('Address', text='Address')

scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=contact_tree.yview)
contact_tree.configure(yscroll=scrollbar.set)

search_label = ttk.Label(frame, text="Search:")
search_entry = ttk.Entry(frame)
search_button = ttk.Button(frame, text="Search", command=search_contact)

status_label = ttk.Label(frame, text="", foreground="green")


name_label.grid(row=0, column=0, sticky=tk.W)
name_entry.grid(row=0, column=1, sticky=tk.W)

phone_label.grid(row=1, column=0, sticky=tk.W)
phone_entry.grid(row=1, column=1, sticky=tk.W)

email_label.grid(row=2, column=0, sticky=tk.W)
email_entry.grid(row=2, column=1, sticky=tk.W)

address_label.grid(row=3, column=0, sticky=tk.W)
address_entry.grid(row=3, column=1, sticky=tk.W)

add_button.grid(row=4, column=0, pady=5)
update_button.grid(row=4, column=1, pady=5)
delete_button.grid(row=4, column=2, pady=5)

contact_tree.grid(row=0, column=2, rowspan=6, columnspan=4, pady=5, padx=(10, 0), sticky=(tk.W, tk.E, tk.N, tk.S))
scrollbar.grid(row=0, column=6, rowspan=6, pady=5, sticky=(tk.W, tk.N, tk.S))

search_label.grid(row=5, column=0, pady=5, sticky=tk.W)
search_entry.grid(row=5, column=1, pady=5, sticky=tk.W)
search_button.grid(row=5, column=2, pady=5)

status_label.grid(row=6, column=0, columnspan=6, pady=(0, 5))


root.mainloop()
