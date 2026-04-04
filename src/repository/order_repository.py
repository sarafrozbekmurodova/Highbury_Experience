"""
Repository abstraction for order data.

The name "OrderRepository" reflects its role as an abstraction layer
for accessing and storing order-related data within the application.

This class defines the contract that all concrete order repository
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


class OrderRepository:
    """
    Abstract base class for order repositories.

    Concrete implementations (e.g. in-memory or database-backed repositories)
    must implement all methods defined here.
    """

    def get_order(self):
        """
        Retrieve the current order.

        :return: Order instance
        """
        raise NotImplementedError

    def save_order(self, order):
        """
        Persist the current order.

        :param order: Order instance to store
        """
        raise NotImplementedError

    def clear_order(self):
        """
        Clear the current order data.
        """
        raise NotImplementedError

    def get_tip_percentage(self):
        """
        Retrieve the current tip percentage.

        :return: Tip percentage as a decimal value
        """
        raise NotImplementedError

    def set_tip_percentage(self, tip_percentage):
        """
        Store the selected tip percentage.

        :param tip_percentage: Tip percentage as a decimal value
        """
        raise NotImplementedError