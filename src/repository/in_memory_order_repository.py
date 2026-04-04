"""
In-memory implementation of the OrderRepository.

The name "InMemoryOrderRepository" reflects that this implementation
stores order data directly in memory using Python objects.

Responsibilities:
- store and retrieve the current order during runtime,
- manage the selected tip percentage,
- provide a simple, fast data source without external dependencies.

Design note:
- This is a concrete implementation of the OrderRepository abstraction.
- It follows the same contract but does not require persistent storage.
- Other implementations (e.g. JSON or database-backed repositories)
  can replace this class without affecting the rest of the application.

Benefits:
- Simple and efficient for development and testing
- No external setup required
- Easily replaceable due to repository abstraction
"""

from model.order import Order
from repository.order_repository import OrderRepository


class InMemoryOrderRepository(OrderRepository):
    """
    Concrete in-memory implementation of the order repository.

    Maintains order state and tip percentage in memory for the duration
    of the application runtime.
    """

    def __init__(self):
        """
        Initialize the in-memory order repository.

        Creates a new empty order and sets the default tip percentage to 0.
        """
        self._current_order = Order()
        self._tip_percentage = 0.0

    def get_order(self):
        """
        Retrieve the current order.

        :return: Order instance
        """
        return self._current_order

    def save_order(self, order):
        """
        Persist the current order in memory.

        :param order: Order instance to store
        """
        self._current_order = order

    def clear_order(self):
        """
        Reset the current order to a new empty instance.
        """
        self._current_order = Order()

    def get_tip_percentage(self):
        """
        Retrieve the current tip percentage.

        :return: Tip percentage as a decimal value
        """
        return self._tip_percentage

    def set_tip_percentage(self, tip_percentage):
        """
        Store the selected tip percentage.

        :param tip_percentage: Tip percentage as a decimal value
        """
        self._tip_percentage = tip_percentage