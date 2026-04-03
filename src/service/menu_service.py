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
    
    def get_item_by_id(self, item_id: str):
        raw_item = self.menu_repository.get_by_id(item_id)
        if not raw_item:
            return None

        return MenuItem(
            name_key=raw_item["name_key"],
            desc_key=raw_item["desc_key"],
            price=raw_item["price"],
            image=raw_item["image"]
        )