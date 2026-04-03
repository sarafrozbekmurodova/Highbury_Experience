from view.pages.menu_category_page import MenuCategoryPage

class DessertsPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        dessert_items = [
            {"name_key": "chocolate_lava_cake", "desc_key": "chocolate_lava_cake_desc", "price": 75, "image": "chocolate_lava.jpg"},
            {"name_key": "tiramisu", "desc_key": "tiramisu_desc", "price": 68, "image": "tiramisu.jpg"},
            {"name_key": "new_york_cheesecake", "desc_key": "new_york_cheesecake_desc", "price": 72, "image": "cheesecake.jpg"},
            {"name_key": "creme_brulee", "desc_key": "creme_brulee_desc", "price": 65, "image": "creme_brulee.jpg"},
            {"name_key": "apple_pie_a_la_mode", "desc_key": "apple_pie_a_la_mode_desc", "price": 59, "image": "apple_pie.jpg"},
            {"name_key": "panna_cotta", "desc_key": "panna_cotta_desc", "price": 62, "image": "panna_cotta.jpg"},
        ]

        super().__init__(parent, controller, dessert_items, category_key="desserts")
