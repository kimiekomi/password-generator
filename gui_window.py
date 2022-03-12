from tkinter import *


class App(Tk):
    def __init__(self, title, width, height):
        super().__init__()

        self.title(title)

        # Center app in screen
        self.window_width = width
        self.window_height = height
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x_coordinate = int((self.screen_width/2) - (self.window_height/2))
        self.y_coordinate = int((self.screen_height/2) - (self.window_width/2))

        # Open app in previos position
        try:
            with open("app.config", "r") as config:
                self.geometry(config.readline())
        
        except:
            self.geometry(f"{self.window_width}x{self.window_height}+{self.x_coordinate}+{self.y_coordinate}")

        self.bind("<Configure>", self.save_position)

    def save_position(self, event):
        with open("app.config", "w") as config:
            config.write(self.geometry())


if __name__ == "__main__":
    app = App(title="Blank Window", width=500, height=700)
    app.mainloop()

