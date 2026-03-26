import tkinter as tk
from view.main_window import MainWindow
from controller.main_controller import MainController
from view.pages.starters_page import StartersPage


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The Highbury Experience")
        self.root.geometry("1000x600")

        self.controller = MainController(self.root)

        # 2. Create the Main Window and pass the controller
        self.main_window = MainWindow(self.root, self.controller)

        # 3. Connect main_window back to controller
        self.controller.set_main_window(self.main_window)

        # 4. Create and register the pages
        self._create_pages()

        # Show Starters page by default
        self.controller.show_page("starters")

    def _create_pages(self):
        starters_page = StartersPage(self.main_window.page_container, self.controller)
        self.controller.register_page("starters", starters_page)


    def run(self):
        self.root.mainloop()
