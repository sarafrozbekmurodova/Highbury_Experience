"""
Repository abstraction for menu data.

The name "MenuRepository" reflects its role as an abstraction layer
for accessing menu data within the application.

This class defines the contract that all concrete menu repository
implementations must follow.

Design note:
- This follows the concept of separating abstraction from implementation,
  similar to interfaces in languages like Java.
- The application depends on this abstraction rather than a specific
  implementation.

Benefits:
- The underlying data source can be changed (e.g. in-memory, JSON, database)
  without affecting the rest of the system.
- This improves flexibility, testability, and maintainability.
"""


class MenuRepository:
    """
    Abstract base class for menu repositories.

    Concrete implementations (e.g. in-memory or database-backed repositories)
    must implement all methods defined here.
    """

    def get_main_courses(self):
        """
        Retrieve main course items.

        :return: Collection of main course items
        """
        raise NotImplementedError

    def get_starters(self):
        """
        Retrieve starter items.

        :return: Collection of starter items
        """
        raise NotImplementedError

    def get_desserts(self):
        """
        Retrieve dessert items.

        :return: Collection of dessert items
        """
        raise NotImplementedError

    def get_drinks(self):
        """
        Retrieve drink items.

        :return: Collection of drink items
        """
        raise NotImplementedError