from model.menu_item import MenuItem


class MenuService:
    def __init__(self, menu_repository):
        self.menu_repository = menu_repository

    def get_main_courses(self):
        raw_items = self.menu_repository.get_main_courses()

        return [
            MenuItem(
                name_key=item["name_key"],
                desc_key=item["desc_key"],
                price=item["price"],
                image=item["image"]
            )
            for item in raw_items
        ]