from repository.menu_repository import MenuRepository


class InMemoryMenuRepository(MenuRepository):

    def get_main_courses(self):
        return [
            {
                "name_key": "steak",
                "desc_key": "steak_desc",
                "price": 189,
                "image": "steak.jpg"
            },
            {
                "name_key": "burger",
                "desc_key": "burger_desc",
                "price": 135,
                "image": "burger.jpg"
            },
        ]

    def get_starters(self):
        return []

    def get_desserts(self):
        return []

    def get_drinks(self):
        return []