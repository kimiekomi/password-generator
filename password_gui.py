from tkinter import *
from tkinter import ttk
from gui_window import App

debug = True
trace = True

class PasswordApplication(App):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)

        # Options: Labels, Entries, and Buttons
        self.options = LabelFrame(self, text="Input")
        self.options.grid(row=0, column=0, padx=20, pady=(20,10))

        self.enter_label = Label(self.options, text="Enter Desired Number of:")
        self.enter_label.grid(row=0, column=0, sticky=W)

        self.letters = IntVar()

        self.letters_label = Label(self.options, text="Letters")
        self.letters_label.grid(row=1, column=0, sticky=E)
        self.letters.set("10")

        self.letters_box = Entry(self.options, width=5)
        self.letters_box.grid(row=1, column=1)

        self.numbers = IntVar()

        self.numbers_label = Label(self.options, text="Numbers")
        self.numbers_label.grid(row=2, column=0, sticky=E)

        self.numbers_box = Entry(self.options, width=5)
        self.numbers_box.grid(row=2, column=1)
        self.numbers.set("1")

        self.specials = IntVar()

        self.specials_label = Label(self.options, text="Special Characters")
        self.specials_label.grid(row=3, column=0, sticky=E)

        self.specials_box = Entry(self.options, width=5)
        self.specials_box.grid(row=3, column=1)
        self.specials.set("1")

        # Results: Labels, Entries, and Buttons
        self.results = LabelFrame(self, text="Output")
        self.results.grid(row=1, column=0, padx=20, pady=(20,10))

        self.password_label = Label(self.results, text="New Password")
        self.password_label.grid(row=1, column=0, sticky=E)

        self.password_box = Entry(self.results, width=15)
        self.password_box.grid(row=1, column=1)

        # Quit program button
        self.close_button = Button(self, text="Close Application", command=self.destroy)
        self.close_button.grid(row=2, column=0, pady=10)


if __name__ == "__main__":
    app = PasswordApplication(title="Password GUI", width=200, height=100)
    app.mainloop()

