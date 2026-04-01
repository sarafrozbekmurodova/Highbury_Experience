import tkinter as tk
from view.main_window import MainWindow
from controller.main_controller import MainController
from view.pages.starters_page import StartersPage
from view.pages.menu_category_page import MenuCategoryPage
from view.pages.light_courses_page import LightCoursesPage
from view.pages.set_meals_page import SetMealsPage
from view.pages.desserts_page import DessertsPage
from view.pages.drinks_page import DrinksPage


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The Crown & Barrel")

        self.root.geometry("1400x850")
        self.root.minsize(1200, 700)
        self.root.configure(bg="#201814")

        self.controller = MainController(self.root)

        # Create main window
        self.main_window = MainWindow(self.root, self.controller)

        # Connect main window back to controller
        self.controller.set_main_window(self.main_window)

        # Create and register pages
        self._create_pages()

        # Start on Home
        self.main_window.show_home()

    def _create_pages(self):
        # Starters
        starters_page = StartersPage(self.main_window.page_container, self.controller)
        self.controller.register_page("starters", starters_page)

        # Main Courses (FIXED INDENTATION)
        main_items = [
            ("Steak", 189, "Grilled steak with fries", "steak.jpg"),
            ("Burger", 135, "Beef burger with cheese", "burger.jpg"),
        ]

        main_page = MenuCategoryPage(
            self.main_window.page_container,
            self.controller,
            title="Main Courses",
            items=main_items
        )

        self.controller.register_page("main", main_page)

        # Light Courses
        light_courses_page = LightCoursesPage(self.main_window.page_container, self.controller)
        self.controller.register_page("light_courses", light_courses_page)

        # Set Meals
        set_meals_page = SetMealsPage(self.main_window.page_container, self.controller)
        self.controller.register_page("set_meals", set_meals_page)

        # Desserts
        desserts_page = DessertsPage(self.main_window.page_container, self.controller)
        self.controller.register_page("desserts", desserts_page)

        # Drinks
        drinks_page = DrinksPage(self.main_window.page_container, self.controller)
        self.controller.register_page("drinks", drinks_page)

    def run(self):
        self.root.mainloop()