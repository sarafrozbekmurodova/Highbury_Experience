# src/controller/main_controller.py

from controller.translations import translations
from service.order_service import OrderService


class MainController:
    def __init__(self, root, menu_service, order_repository):
        self.root = root
        self.main_window = None
        self.pages = {}
        self.translations = translations
        self.menu_service = menu_service
        self.order_repository = order_repository
        self.order_service = OrderService(order_repository)

    def t(self, key):
        lang = getattr(self.main_window, "current_language", "en")
        return self.main_window.translations.get(lang, {}).get(key, key)

    def set_main_window(self, main_window):
        self.main_window = main_window

    def register_page(self, name: str, page_frame):
        self.pages[name] = page_frame
        page_frame.grid(row=0, column=0, sticky="nsew")

    def initialize_pages(self, page_container):
        from view.pages.starters_page import StartersPage
        from view.pages.menu_category_page import MenuCategoryPage
        from view.pages.light_courses_page import LightCoursesPage
        from view.pages.set_meals_page import SetMealsPage
        from view.pages.desserts_page import DessertsPage
        from view.pages.drinks_page import DrinksPage

        # Starters
        starters_page = StartersPage(page_container, self)
        self.register_page("starters", starters_page)

        # Main courses from service
        main_items = self.menu_service.get_main_courses()
        main_page = MenuCategoryPage(
            page_container,
            self,
            main_items,
            "main_courses"
        )
        self.register_page("main", main_page)

        # Light Courses
        light_courses_page = LightCoursesPage(page_container, self)
        self.register_page("light_courses", light_courses_page)

        # Set Meals
        set_meals_page = SetMealsPage(page_container, self)
        self.register_page("set_meals", set_meals_page)

        # Desserts
        desserts_page = DessertsPage(page_container, self)
        self.register_page("desserts", desserts_page)

        # Drinks
        drinks_page = DrinksPage(page_container, self)
        self.register_page("drinks", drinks_page)

    def show_page(self, name: str):
        if name in self.pages:
            self.main_window.show_page(self.pages[name])
        else:
            print(f"Page '{name}' is not implemented yet.")

    # -----------------------------
    # Order Use Case
    # -----------------------------

    def add_to_order(self, item_data):
        """
        item_data is expected to be a dict, for example:
        {
            "item_id": "grilled_salmon",
            "name": "Grilled Salmon",
            "price": 189
        }

        Fallbacks are supported in OrderService if item_id is missing.
        """
        try:
            self.order_service.add_item(item_data)
            self.refresh_order_panel()
        except Exception as e:
            print(f"Error adding item: {e}")

    def change_quantity(self, item_id: str, delta: int):
        self.order_service.change_quantity(item_id, delta)
        self.refresh_order_panel()

    def remove_from_order(self, item_id: str):
        self.order_service.remove_item(item_id)
        self.refresh_order_panel()

    def get_subtotal(self):
        return self.order_service.get_total()

    def get_tip_amount(self):
        subtotal = self.get_subtotal()
        return round(subtotal * self.order_repository.get_tip_percentage())

    def get_total(self):
        return self.get_subtotal() + self.get_tip_amount()

    def set_tip_percentage(self, tip_percentage: float):
        self.order_repository.set_tip_percentage(tip_percentage)
        self.refresh_order_panel()

    def place_order(self):
        if self.order_service.is_empty():
            print("Order is empty!")
            return

        order_items, subtotal = self.order_service.place_order()
        total = self.get_total()
        tip_percentage = self.order_repository.get_tip_percentage()

        print(f"Order placed! Subtotal: {subtotal} kr, Total: {total} kr")
        print("Items:", order_items)

        if self.main_window:
            self.main_window.show_confirmation_page(
                order_items,
                subtotal,
                total,
                tip_percentage
            )

        self.order_service.clear_order()
        self.refresh_order_panel()

    def refresh_order_panel(self):
        if self.main_window:
            order_items, subtotal = self.order_service.get_order_summary()
            total = subtotal + round(subtotal * self.order_repository.get_tip_percentage())

            self.main_window.update_order_list(
                order_items,
                subtotal,
                total,
                self.order_repository.get_tip_percentage()
            )