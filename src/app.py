import tkinter as tk
from view.main_window import MainWindow
from controller.main_controller import MainController
from repository.in_memory_menu_repository import InMemoryMenuRepository
from repository.in_memory_order_repository import InMemoryOrderRepository


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The Crown & Barrel")

        self.root.geometry("1400x850")
        self.root.minsize(1200, 700)
        self.root.configure(bg="#201814")

        self.controller = MainController(
            self.root,
            InMemoryMenuRepository(),
            InMemoryOrderRepository()
        )

        # Create main window
        self.main_window = MainWindow(self.root, self.controller)

        # Connect main window back to controller
        self.controller.set_main_window(self.main_window)

        # Let controller create and register pages
        self.controller.initialize_pages(self.main_window.page_container)

        # Start on Home
        self.main_window.show_home()

    def run(self):
        self.root.mainloop()