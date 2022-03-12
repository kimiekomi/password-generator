from tkinter import *
from tkinter import ttk
from gui_window import App

debug = True
trace = True


class PasswordApplication(App):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)


if __name__ == "__main__":
    app = PasswordApplication(title="Password GUI", width=200, height=100)
    app.mainloop()

