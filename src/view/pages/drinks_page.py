from view.pages.menu_category_page import MenuCategoryPage


class DrinksPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        drink_items = [
            {
                "item_id": "drink_espresso",
                "name_key": "espresso",
                "desc_key": "espresso_desc",
                "price": 35,
                "image": "espresso.jpg"
            },
            {
                "item_id": "drink_cappuccino",
                "name_key": "cappuccino",
                "desc_key": "cappuccino_desc",
                "price": 45,
                "image": "cappuccino.jpg"
            },
            {
                "item_id": "drink_fresh_orange_juice",
                "name_key": "fresh_orange_juice",
                "desc_key": "fresh_orange_juice_desc",
                "price": 48,
                "image": "orange_juice.jpg"
            },
            {
                "item_id": "drink_house_red_wine",
                "name_key": "house_red_wine",
                "desc_key": "house_red_wine_desc",
                "price": 89,
                "image": "red_wine.jpg"
            },
            {
                "item_id": "drink_house_white_wine",
                "name_key": "house_white_wine",
                "desc_key": "house_white_wine_desc",
                "price": 85,
                "image": "white_wine.jpg"
            },
            {
                "item_id": "drink_craft_beer",
                "name_key": "craft_beer",
                "desc_key": "craft_beer_desc",
                "price": 65,
                "image": "beer.jpg"
            },
        ]

        super().__init__(
            parent,
            controller,
            drink_items,
            category_key="drinks"
        )