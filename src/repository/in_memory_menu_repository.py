class InMemoryMenuRepository:
    def get_main_courses(self):
        return [
            {
                "item_id": "main_steak",
                "name_key": "steak",
                "desc_key": "steak_desc",
                "price": 189,
                "image": "steak.jpg"
            },
            {
                "item_id": "main_burger",
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

    def get_all(self):
        return (
            self.get_main_courses()
            + self.get_starters()
            + self.get_desserts()
            + self.get_drinks()
        )