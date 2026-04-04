"""
Application bootstrap and composition root.

Responsibilities:
- Initialize the Tkinter root window
- Create and wire together all core components:
  - Repositories (data layer)
  - Services (business logic)
  - Controller (application logic)
  - MainWindow (UI / View)
- Start the application

Architecture:
- Follows a simplified MVC structure
- This file is responsible for dependency injection (manual)
"""

import tkinter as tk
from view.main_window import MainWindow
from controller.main_controller import MainController
from repository.in_memory_menu_repository import InMemoryMenuRepository
from repository.in_memory_order_repository import InMemoryOrderRepository
from service.menu_service import MenuService


class App:
    """
    Main application class.

    Acts as the entry point for setting up the system and starting the UI loop.
    """

    def __init__(self):
        """
        Initialize application components and wire dependencies.
        """
        self.root = tk.Tk()
        self.root.title("The Crown & Barrel")

        self.root.geometry("1400x850")
        self.root.minsize(1200, 700)
        self.root.configure(bg="#201814")

        # ---------- Data Layer ----------
        menu_repository = InMemoryMenuRepository()
        order_repository = InMemoryOrderRepository()

        # ---------- Service Layer ----------
        menu_service = MenuService(menu_repository)

        # ---------- Controller ----------
        self.controller = MainController(
            self.root,
            menu_service,
            order_repository
        )

        # ---------- View ----------
        self.main_window = MainWindow(self.root, self.controller)

        # Connect View <-> Controller
        self.controller.set_main_window(self.main_window)

        # Initialize pages inside the main window
        self.controller.initialize_pages(self.main_window.page_container)

        # Start on Home page
        self.main_window.show_home()

    def run(self):
        """
        Start the Tkinter main event loop.
        """
        self.root.mainloop()