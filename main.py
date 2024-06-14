import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

        # GUI Elements
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.contact_listbox = tk.Listbox(self.frame, width=50, height=15)
        self.contact_listbox.pack(side=tk.LEFT, padx=10)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contact_listbox.yview)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.view_button = tk.Button(self.button_frame, text="View Contact", command=self.view_contact)
        self.view_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if name:
            phone = simpledialog.askstring("Input", "Enter contact phone number:")
            if phone:
                self.contacts[name] = phone
                self.update_contact_list()

    def view_contact(self):
        selected_contact = self.contact_listbox.curselection()
        if selected_contact:
            name = self.contact_listbox.get(selected_contact)
            phone = self.contacts[name]
            messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {phone}")
        else:
            messagebox.showwarning("View Contact", "No contact selected.")

    def delete_contact(self):
        selected_contact = self.contact_listbox.curselection()
        if selected_contact:
            name = self.contact_listbox.get(selected_contact)
            del self.contacts[name]
            self.update_contact_list()
        else:
            messagebox.showwarning("Delete Contact", "No contact selected.")

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for name in self.contacts:
            self.contact_listbox.insert(tk.END, name)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
