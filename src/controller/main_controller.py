# src/controller/main_controller.py

from controller.translations import translations


class MainController:
    def __init__(self, root, menu_service, order_repository):
        self.root = root
        self.main_window = None
        self.pages = {}
        self.translations = translations
        self.menu_service = menu_service
        self.order_repository = order_repository

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

    def add_to_order(self, item_name: str, price: int):
        try:
            order = self.order_repository.get_order()

            for item in order:
                if item["name"] == item_name:
                    item["quantity"] += 1
                    self.refresh_order_panel()
                    return

            order.append({
                "name": item_name,
                "price": price,
                "quantity": 1
            })
            self.refresh_order_panel()
        except Exception as e:
            print(f"Error adding item: {e}")

    def change_quantity(self, index: int, delta: int):
        order = self.order_repository.get_order()
        if 0 <= index < len(order):
            order[index]["quantity"] += delta
            if order[index]["quantity"] <= 0:
                del order[index]
            self.refresh_order_panel()

    def remove_from_order(self, index: int):
        order = self.order_repository.get_order()
        if 0 <= index < len(order):
            del order[index]
            self.refresh_order_panel()

    def get_subtotal(self):
        order = self.order_repository.get_order()
        return sum(item["price"] * item["quantity"] for item in order)

    def get_tip_amount(self):
        return round(self.get_subtotal() * self.order_repository.get_tip_percentage())

    def get_total(self):
        return self.get_subtotal() + self.get_tip_amount()

    def set_tip_percentage(self, tip_percentage: float):
        self.order_repository.set_tip_percentage(tip_percentage)
        self.refresh_order_panel()

    def place_order(self):
        order = self.order_repository.get_order()

        if not order:
            print("Order is empty!")
            return

        subtotal = self.get_subtotal()
        total = self.get_total()
        tip_percentage = self.order_repository.get_tip_percentage()

        print(f"Order placed! Subtotal: {subtotal} kr, Total: {total} kr")
        print("Items:", order)

        self.main_window.show_confirmation_page(
            order,
            subtotal,
            total,
            tip_percentage
        )

        self.order_repository.clear_order()
        self.refresh_order_panel()

    def refresh_order_panel(self):
        if self.main_window:
            self.main_window.update_order_list(
                self.order_repository.get_order(),
                self.get_subtotal(),
                self.get_total(),
                self.order_repository.get_tip_percentage()
            )