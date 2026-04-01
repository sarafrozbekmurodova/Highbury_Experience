from view.pages.menu_category_page import MenuCategoryPage


class DrinksPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        drink_items = [
            ("Espresso", "35 kr", "Freshly brewed Italian espresso", "espresso.jpg"),
            ("Cappuccino", "45 kr", "With velvety milk foam", "cappuccino.jpg"),
            ("Fresh Orange Juice", "48 kr", "Freshly squeezed", "orange_juice.jpg"),
            ("House Red Wine", "89 kr", "Glass of Cabernet Sauvignon", "red_wine.jpg"),
            ("House White Wine", "85 kr", "Glass of Chardonnay", "white_wine.jpg"),
            ("Craft Beer", "65 kr", "Local IPA", "beer.jpg"),
        ]

        super().__init__(parent, controller, title="Drinks", items=drink_items)