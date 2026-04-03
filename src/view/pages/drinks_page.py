from view.pages.menu_category_page import MenuCategoryPage

class DrinksPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        drink_items = [
            {"name_key": "espresso", "desc_key": "espresso_desc", "price": 35, "image": "espresso.jpg"},
            {"name_key": "cappuccino", "desc_key": "cappuccino_desc", "price": 45, "image": "cappuccino.jpg"},
            {"name_key": "fresh_orange_juice", "desc_key": "fresh_orange_juice_desc", "price": 48, "image": "orange_juice.jpg"},
            {"name_key": "house_red_wine", "desc_key": "house_red_wine_desc", "price": 89, "image": "red_wine.jpg"},
            {"name_key": "house_white_wine", "desc_key": "house_white_wine_desc", "price": 85, "image": "white_wine.jpg"},
            {"name_key": "craft_beer", "desc_key": "craft_beer_desc", "price": 65, "image": "beer.jpg"},
        ]

        super().__init__(parent, controller, drink_items, category_key="drinks")
