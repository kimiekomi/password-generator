from tkinter import *
from tkinter import ttk
from gui_window import App
from password_generator import password_generator

debug = True
trace = True

class PasswordApplication(App):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)

        # Input Labels and Entries
        self.enter_label = Label(self, text="Enter Desired Number of:")
        self.enter_label.grid(row=0, column=0, pady=10, sticky=W)

        self.letters = IntVar()

        self.letters_label = Label(self, text="Letters")
        self.letters_label.grid(row=1, column=0, sticky=E)

        self.letters_box = Entry(self, width=5)
        self.letters_box.grid(row=1, column=1)
        self.letters_box.insert(0, "10")

        self.numbers = IntVar()

        self.numbers_label = Label(self, text="Numbers")
        self.numbers_label.grid(row=2, column=0, sticky=E)

        self.numbers_box = Entry(self, width=5)
        self.numbers_box.grid(row=2, column=1)
        self.numbers_box.insert(0, "1")

        self.specials = IntVar()

        self.specials_label = Label(self, text="Special Characters")
        self.specials_label.grid(row=3, column=0, sticky=E)

        self.specials_box = Entry(self, width=5)
        self.specials_box.grid(row=3, column=1)
        self.specials_box.insert(0, "1")

        # Error label
        self.error_label = Label(self, text=">>> ERROR: Values must be integers")
        self.error_label.grid(row=4, column=0, padx=20, sticky=W)
        self.error_label.grid_remove()
        
        # Output Labels and Entries
        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=5, column=0, sticky=E)
        
        self.password_box = Entry(self, width=15)
        self.password_box.grid(row=5, column=1)

        # Buttons
        self.clear_button = Button(self, text="Clear", command=self.clear_entries)
        self.clear_button.grid(row=1, column=2, pady=(0,10))

        self.submit_button = Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, column=2, pady=(0,10))

        self.save_button = Button(self, text="Save", command=self.save_password)
        self.save_button.grid(row=6, column=0, pady=(0,10))

        self.close_button = Button(self, text="Close Application", command=self.destroy)
        self.close_button.grid(row=7, column=0, pady=(0,10))


    def clear_entries(self):
        self.letters_box.delete(0, END)
        self.numbers_box.delete(0, END)
        self.specials_box.delete(0, END)
        self.password_box.delete(0, END)

        self.letters_box.insert(0, "10")
        self.numbers_box.insert(0, "1")
        self.specials_box.insert(0, "1")


    def save_password(self):
        pass

    def submit(self):
        try:
            number_of_letters = int(self.letters_box.get())
            number_of_numbers = int(self.numbers_box.get())
            number_of_specials = int(self.specials_box.get())

        except ValueError:
            self.error_label.grid(row=4, column=0, padx=20, sticky=W)
            return

        results = password_generator(number_of_letters, number_of_numbers, number_of_specials)
        self.display_results(results)

    def display_results(self, results):
        self.password_box.delete(0, "end")
        self.password_box.insert(0, results)


if __name__ == "__main__":
    app = PasswordApplication(title="Password GUI", width=200, height=100)
    app.mainloop()

