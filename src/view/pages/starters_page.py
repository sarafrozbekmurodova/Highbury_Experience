from view.pages.menu_category_page import MenuCategoryPage


class StartersPage(MenuCategoryPage):
    def __init__(self, parent, controller):
        items = [
            {
                "item_id": "starter_bruschetta",
                "name_key": "starter_bruschetta",
                "desc_key": "starter_bruschetta_desc",
                "price": 48,
                "image": "bruschetta.jpg"
            },
            {
                "item_id": "starter_caesar",
                "name_key": "starter_caesar",
                "desc_key": "starter_caesar_desc",
                "price": 65,
                "image": "caesar_salad.jpg"
            },
            {
                "item_id": "starter_garlic",
                "name_key": "starter_garlic",
                "desc_key": "starter_garlic_desc",
                "price": 39,
                "image": "garlic_bread.jpg"
            },
            {
                "item_id": "starter_soup",
                "name_key": "starter_soup",
                "desc_key": "starter_soup_desc",
                "price": 52,
                "image": "soup.jpg"
            },
            {
                "item_id": "starter_calamari",
                "name_key": "starter_calamari",
                "desc_key": "starter_calamari_desc",
                "price": 89,
                "image": "calamari.jpg"
            }
        ]

        super().__init__(
            parent,
            controller,
            items,
            category_key="starters"
        )