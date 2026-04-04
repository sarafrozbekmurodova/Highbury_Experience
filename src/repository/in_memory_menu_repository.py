"""
In-memory implementation of the MenuRepository.

The name "InMemoryMenuRepository" reflects that this implementation stores
and provides menu data directly in memory using Python data structures.

Responsibilities:
- provide menu data without external storage,
- serve as a simple and fast data source for development and testing.

Design note:
- This is a concrete implementation of the MenuRepository abstraction.
- It follows the same contract but does not require any external system
  such as a database or file storage.

Benefits:
- Simple and fast for development
- No external dependencies
- Can easily be replaced with other implementations (e.g. JSON or database)
  without affecting the rest of the application
"""


class InMemoryMenuRepository:
    """
    Concrete in-memory implementation of the menu repository.

    Returns static menu data stored as Python dictionaries.
    """

    def get_main_courses(self):
        """
        Retrieve main course items stored in memory.

        :return: List of main course items
        """
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
        """
        Retrieve starter items.

        Currently returns an empty list because starters are defined elsewhere.
        """
        return []

    def get_desserts(self):
        """
        Retrieve dessert items.

        Currently returns an empty list because desserts are defined elsewhere.
        """
        return []

    def get_drinks(self):
        """
        Retrieve drink items.

        Currently returns an empty list because drinks are defined elsewhere.
        """
        return []

    def get_all(self):
        """
        Retrieve all menu items across categories.

        :return: Combined list of all menu items
        """
        return (
            self.get_main_courses()
            + self.get_starters()
            + self.get_desserts()
            + self.get_drinks()
        )