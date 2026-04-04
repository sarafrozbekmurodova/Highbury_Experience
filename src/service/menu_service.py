"""
Menu service layer.

The name "MenuService" reflects its role as the service responsible for
retrieving and transforming menu data from the repository layer into
MenuItem model objects used by the application.

Responsibilities:
- retrieve menu item data from the repository,
- convert raw repository data into MenuItem objects,
- provide menu data access to the controller.

Note:
- In the current implementation, this service is primarily used for
  repository-backed main course items.
"""

from model.menu_item import MenuItem


class MenuService:
    """
    Service class responsible for menu-related data access and transformation.
    """

    def __init__(self, menu_repository):
        """
        Initialize the menu service.

        :param menu_repository: Repository providing raw menu item data
        """
        self.menu_repository = menu_repository

    def get_main_courses(self):
        """
        Retrieve main course items from the repository and convert them to MenuItem objects.

        :return: List of MenuItem instances
        """
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
        """
        Retrieve a single menu item by its identifier.

        :param item_id: Identifier of the requested menu item
        :return: MenuItem instance if found, otherwise None
        """
        raw_item = self.menu_repository.get_by_id(item_id)
        if not raw_item:
            return None

        return MenuItem(
            name_key=raw_item["name_key"],
            desc_key=raw_item["desc_key"],
            price=raw_item["price"],
            image=raw_item["image"]
        )