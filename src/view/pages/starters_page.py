from view.pages.menu_category_page import MenuCategoryPage


class StartersPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        starter_items = [
            ("Classic Bruschetta", 48, "Toasted bread with tomatoes & basil", "bruschetta.jpg"),
            ("Caesar Salad", 65, "Romaine, parmesan & croutons", "caesar_salad.jpg"),
            ("Garlic Bread with Cheese", 39, "Freshly baked with mozzarella", "garlic_bread.jpg"),
            ("Soup of the Day", 52, "Ask staff for today's special", "soup.jpg"),
            ("Fried Calamari", 89, "With lemon aioli", "calamari.jpg"),
        ]

        super().__init__(parent, controller, title="Starters", items=starter_items)