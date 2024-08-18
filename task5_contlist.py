import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")
        self.master.geometry("500x400")
        self.master.configure(bg="#424242")

        self.contacts = {}

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Contact Manager", font=("Verdana", 18), bg="#424242", fg="#ffffff").pack(pady=10)

        self.add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact, font=("Verdana", 14), bg="#00bcd4", fg="#ffffff")
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.master, text="View Contacts", command=self.view_contacts, font=("Verdana", 14), bg="#00bcd4", fg="#ffffff")
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(self.master, text="Search Contact", command=self.search_contact, font=("Verdana", 14), bg="#00bcd4", fg="#ffffff")
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(self.master, text="Update Contact", command=self.update_contact, font=("Verdana", 14), bg="#00bcd4", fg="#ffffff")
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.master, text="Delete Contact", command=self.delete_contact, font=("Verdana", 14), bg="#00bcd4", fg="#ffffff")
        self.delete_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email address:")
        address = simpledialog.askstring("Input", "Enter address:")

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", f"Contact {name} added successfully!")
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required.")

    def view_contacts(self):
        contacts_list = "\n".join([f"{name}: {info['phone']}" for name, info in self.contacts.items()])
        messagebox.showinfo("Contacts List", contacts_list if contacts_list else "No contacts found.")

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter contact name or phone number:")
        found_contacts = [f"{name}: {info['phone']}" for name, info in self.contacts.items() if search_term in name or search_term in info['phone']]
        messagebox.showinfo("Search Results", "\n".join(found_contacts) if found_contacts else "No matching contacts found.")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name to update:")
        if name in self.contacts:
            phone = simpledialog.askstring("Input", f"Enter new phone number (current: {self.contacts[name]['phone']}):")
            email = simpledialog.askstring("Input", f"Enter new email address (current: {self.contacts[name].get('email', 'N/A')}):")
            address = simpledialog.askstring("Input", f"Enter new address (current: {self.contacts[name].get('address', 'N/A')}):")

            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", f"Contact {name} updated successfully!")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
