from tkinter import *
from tkinter import ttk
from gui_window import App
from password_generator import password_generator
from database import Database

debug = True
trace = True

class PasswordApplication(App):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)

        # Input Labels and Entries
        self.enter_label = Label(self, text="Enter Desired Number of:")
        self.enter_label.grid(row=0, column=0, columnspan=2, padx=(20,0), pady=(20,0), sticky=W)

        self.letters = IntVar()

        self.letters_label = Label(self, text="Letters")
        self.letters_label.grid(row=1, column=0, sticky=E)

        self.letters_box = Entry(self, width=5)
        self.letters_box.grid(row=1, column=1, padx=10, sticky=W)
        self.letters_box.insert(0, "10")

        self.numbers = IntVar()

        self.numbers_label = Label(self, text="Numbers")
        self.numbers_label.grid(row=2, column=0, sticky=E)

        self.numbers_box = Entry(self, width=5)
        self.numbers_box.grid(row=2, column=1, padx=10, sticky=W)
        self.numbers_box.insert(0, "1")

        self.specials = IntVar()

        self.specials_label = Label(self, text="Special Characters")
        self.specials_label.grid(row=3, column=0, sticky=E)

        self.specials_box = Entry(self, width=5)
        self.specials_box.grid(row=3, column=1, padx=10, sticky=W)
        self.specials_box.insert(0, "1")

        # Blank and Error label
        self.blank_label = Label(self, text=" ")
        self.blank_label.grid(row=4, column=0, columnspan=3, padx=30, sticky=W)

        self.error_label = Label(self, text=">>> ERROR: All values must be integers", fg="red")
        self.error_label.grid(row=4, column=0, columnspan=3, padx=30, sticky=W)
        self.error_label.grid_remove()
        
        # Output: Labels, Entries, and Button
        self.output = LabelFrame(self, text="Output")
        self.output.grid(row=5, column=0, columnspan=4, padx=20, pady=(10,15))

        self.password_label = Label(self.output, text="New Password")
        self.password_label.grid(row=0, column=0, padx=10, sticky=E)
        
        self.password_box = Entry(self.output, width=25)
        self.password_box.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        self.website_label = Label(self.output, text="Website Name")
        self.website_label.grid(row=1, column=0, padx=10, pady=(0,10), sticky=E)
        
        self.website_box = Entry(self.output, width=25)
        self.website_box.grid(row=1, column=1, padx=10, pady=(0,10),sticky=W)
        self.website_box.insert(0, "N/A")

        self.add_button = Button(self.output, text="Add to Database", command=self.add_entry)
        self.add_button.grid(row=2, column=0, columnspan=4, padx=10, pady=(0,20), ipadx=130)

        # Buttons
        self.reset_button = Button(self, text="Reset", command=self.reset_fields)
        self.reset_button.grid(row=1, column=1, padx=(100,0), pady=(10,0), ipadx=25, ipady=5)

        self.submit_button = Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, column=1, padx=(100,0), pady=(0,0), ipadx=20, ipady=5)

        self.close_button = Button(self, text="Close Application", command=self.destroy)
        self.close_button.grid(row=10, column=0, columnspan=4, padx=8, pady=(5,10), ipadx=143, ipady=2)

        # Database
        self.database = LabelFrame(self, text="Database")
        self.database.grid(row=6, column=0, columnspan=4, padx=20, pady=(0,10))

        self.update_button = Button(self.database, text="Update", command=self.update_entry)
        self.update_button.grid(row=1, column=0, padx=(30,0), pady=10, ipadx=10)

        self.remove_button = Button(self.database, text="Remove", command=self.remove_entry)
        self.remove_button.grid(row=1, column=1, padx=(10,0), pady=10, ipadx=10)

        self.delete_button = Button(self.database, text="Delete ALL", command=self.delete_database)
        self.delete_button.grid(row=1, column=2, padx=10, pady=10, ipadx=10)

        # Password Tree
        self.password_tree = ttk.Treeview(self.database, height=13)
        self.password_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=(10,0))

        # Columns
        self.password_tree["columns"] = ("ID", "Website Name", "Password")

        # Format columns
        self.password_tree.column("#0", width=0, minwidth=0, stretch=NO)
        self.password_tree.column("ID", anchor=CENTER, width=30)
        self.password_tree.column("Website Name", anchor=W, width=155)
        self.password_tree.column("Password", anchor=W, width=215)

        # Headings
        self.password_tree.heading("#0", text="", anchor=W)
        self.password_tree.heading("ID", text="ID", anchor=CENTER)
        self.password_tree.heading("Website Name", text="Website Name", anchor=W)
        self.password_tree.heading("Password", text="Password", anchor=W)

        # Scrollbar
        self.scrollbar = Scrollbar(self.database)
        self.scrollbar.grid(row=0, column=3, padx=(0, 10), pady=(35,0), sticky=N+S+E)

        # Attach scrollbar to address_list
        self.password_tree.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.password_tree.yview)

    def reset_fields(self):
        self.letters_box.delete(0, END)
        self.numbers_box.delete(0, END)
        self.specials_box.delete(0, END)
        self.password_box.delete(0, END)

        self.letters_box.insert(0, "10")
        self.numbers_box.insert(0, "1")
        self.specials_box.insert(0, "1")

        self.error_label.grid_remove()
        

    def submit(self):
        if debug: print("initialized submit()")

        try:
            number_of_letters = int(self.letters_box.get())
            number_of_numbers = int(self.numbers_box.get())
            number_of_specials = int(self.specials_box.get())

        except ValueError:
            self.error_label.grid(row=4, column=0, columnspan=3, padx=30, sticky=W)
            return

        results = password_generator(number_of_letters, number_of_numbers, number_of_specials)

        if trace: print(f"results - {results}")

        self.display_results(results)
        self.error_label.grid_remove()


    def display_results(self, password):
        self.password_box.delete(0, "end")
        self.password_box.insert(0, password)

    def fetch_entries(self):
        if debug: print("initialized fetch_entries()")



    def add_entry(self):
        if debug: print("initialized add_entry()")

        with open("passwords.txt", "a") as file:
            file.write(f"{self.website_box.get()}: {self.password_box.get()}\n")

        self.password_tree.insert(parent="", index="end", text="", values=(self.website_box.get(), self.password_box.get()))


    def update_entry(self):
        pass

    def remove_entry(self):
        pass

    def delete_database(self):
        pass


if __name__ == "__main__":
    app = PasswordApplication(title="Password GUI", width=461, height=761)
    app.mainloop()

