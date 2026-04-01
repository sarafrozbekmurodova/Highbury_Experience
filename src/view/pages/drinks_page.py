from view.pages.menu_category_page import MenuCategoryPage


class DrinksPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        drink_items = [
            ("Espresso", 35, "Freshly brewed Italian espresso", "espresso.jpg"),
            ("Cappuccino", 45, "With velvety milk foam", "cappuccino.jpg"),
            ("Fresh Orange Juice", 48, "Freshly squeezed", "orange_juice.jpg"),
            ("House Red Wine", 89, "Glass of Cabernet Sauvignon", "red_wine.jpg"),
            ("House White Wine", 85, "Glass of Chardonnay", "white_wine.jpg"),
            ("Craft Beer", 65, "Local IPA", "beer.jpg"),
        ]

        super().__init__(parent, controller, title="Drinks", items=drink_items)