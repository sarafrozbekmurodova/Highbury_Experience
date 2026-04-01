from view.pages.menu_category_page import MenuCategoryPage


class DessertsPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        dessert_items = [
            ("Chocolate Lava Cake", 75, "Warm chocolate cake with molten center & vanilla ice cream", "chocolate_lava.jpg"),
            ("Tiramisu", 68, "Classic Italian coffee-flavored dessert", "tiramisu.jpg"),
            ("New York Cheesecake", 72, "With strawberry coulis", "cheesecake.jpg"),
            ("Crème Brûlée", 65, "Vanilla custard with caramelized sugar", "creme_brulee.jpg"),
            ("Apple Pie à la Mode", 59, "Warm apple pie served with vanilla ice cream", "apple_pie.jpg"),
            ("Panna Cotta", 62, "With berry compote", "panna_cotta.jpg"),
        ]

        super().__init__(parent, controller, title="Desserts", items=dessert_items)