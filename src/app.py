import tkinter as tk
from view.main_window import MainWindow


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The Highbury Experience")
        self.root.geometry("1000x600")

        self.main_window = MainWindow(self.root)

    def run(self):
        self.root.mainloop()
