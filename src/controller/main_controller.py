"""
Main application controller.

Responsibilities:
- Coordinate interaction between the View and the underlying services
- Handle page registration and navigation
- Manage order-related user actions
- Provide translated text lookup for the UI

Architecture:
- Acts as the Controller in the MVC-inspired design
- Delegates business logic to services and data persistence to repositories
"""

from i18n.translations import translations
from service.order_service import OrderService


class MainController:
    """
    Central controller for the application.

    This class connects the user interface to the service and repository layers.
    """

    def __init__(self, root, menu_service, order_repository):
        """
        Initialize controller dependencies and application state.

        :param root: Tkinter root window
        :param menu_service: Service used to retrieve menu data
        :param order_repository: Repository used to store order state
        """
        self.root = root
        self.main_window = None
        self.order_items = []
        self.pages = {}
        self.translations = translations
        self.menu_service = menu_service
        self.order_repository = order_repository
        self.order_service = OrderService(order_repository)

    def t(self, key):
        """
        Return translated text for the current language.

        :param key: Translation key
        :return: Translated string, or the key itself if missing
        """
        lang = getattr(self.main_window, "current_language", "en")
        return self.main_window.translations.get(lang, {}).get(key, key)

    def set_main_window(self, main_window):
        """
        Attach the main window to the controller.

        :param main_window: Main UI window
        """
        self.main_window = main_window

    def register_page(self, name: str, page_frame):
        """
        Register a page frame and prepare it for stacked-frame navigation.

        :param name: Internal page name
        :param page_frame: Tkinter frame representing the page
        """
        self.pages[name] = page_frame
        page_frame.grid(row=0, column=0, sticky="nsew")

    def initialize_pages(self, page_container):
        """
        Create and register all page views used by the application.

        :param page_container: Parent container holding the page frames
        """
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
        """
        Show a registered page in the main window.

        :param name: Name of the page to display
        """
        if name in self.pages:
            self.main_window.show_page(self.pages[name])
        else:
            print(f"Page '{name}' is not implemented yet.")

    def add_to_order(self, item_data):
        """
        Add an item to the current order and refresh the order panel.

        :param item_data: Dictionary containing item information
        """
        self.order_service.add_item(item_data)
        self.refresh_order_panel()

    def change_quantity(self, item_id: str, delta: int):
        """
        Change the quantity of an order item and refresh the order panel.

        :param item_id: Identifier of the item
        :param delta: Quantity change, typically +1 or -1
        """
        self.order_service.change_quantity(item_id, delta)
        self.refresh_order_panel()

    def remove_from_order(self, item_id: str):
        """
        Remove an item from the order and refresh the order panel.

        :param item_id: Identifier of the item to remove
        """
        self.order_service.remove_item(item_id)
        self.refresh_order_panel()

    def get_subtotal(self):
        """
        Return the current subtotal before tip.

        :return: Subtotal amount
        """
        return self.order_service.get_total()

    def get_tip_amount(self):
        """
        Calculate the tip amount based on the current subtotal.

        :return: Tip amount
        """
        subtotal = self.get_subtotal()
        return round(subtotal * self.order_repository.get_tip_percentage())

    def get_total(self):
        """
        Return the total amount including tip.

        :return: Total amount
        """
        return self.get_subtotal() + self.get_tip_amount()

    def set_tip_percentage(self, tip_percentage: float):
        """
        Update the tip percentage and refresh the order panel.

        :param tip_percentage: Tip percentage as a decimal value
        """
        self.order_repository.set_tip_percentage(tip_percentage)
        self.refresh_order_panel()

    def place_order(self):
        """
        Finalize the current order, show confirmation, then clear the order.
        """
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
        """
        Refresh the order summary shown in the UI.
        """
        if self.main_window:
            order_items, subtotal = self.order_service.get_order_summary()
            total = subtotal + round(subtotal * self.order_repository.get_tip_percentage())

            self.main_window.update_order_list(
                order_items,
                subtotal,
                total,
                self.order_repository.get_tip_percentage()
            )