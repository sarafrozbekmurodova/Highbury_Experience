"""
Order service layer.

The name "OrderService" reflects its role as the service responsible for
handling all order-related operations. In the application's architecture,
a "service" encapsulates business logic and coordinates between the
controller and the data layer (repository).

Responsibilities:
- add, remove, and update order items,
- calculate totals and summaries,
- coordinate persistence via the OrderRepository,
- provide order data in a format suitable for the view layer.

This class does not manage UI state and does not render anything.
"""

from repository.order_repository import OrderRepository


class OrderService:
    """
    Service class responsible for order-related business logic.

    It acts as a bridge between the controller and the order repository.
    """

    def __init__(self, order_repository: OrderRepository):
        """
        Initialize the order service.

        :param order_repository: Repository responsible for storing and retrieving the order
        """
        self.order_repository = order_repository

    def add_item(self, item_data: dict) -> None:
        """
        Add an item to the order.

        :param item_data: Dictionary containing item details (id, name, price, etc.)
        """
        order = self.order_repository.get_order()

        item_id = item_data.get("item_id") or item_data.get("name_key") or item_data["name"]
        name_key = item_data.get("name_key")
        name = item_data["name"]
        price = item_data["price"]

        order.add_item(item_id=item_id, name=name, price=price, name_key=name_key)
        self.order_repository.save_order(order)

    def change_quantity(self, item_id: str, delta: int) -> None:
        """
        Change the quantity of an item in the order.

        :param item_id: Identifier of the item
        :param delta: Quantity change (e.g., +1 or -1)
        """
        order = self.order_repository.get_order()
        order.change_quantity(item_id, delta)
        self.order_repository.save_order(order)

    def remove_item(self, item_id: str) -> None:
        """
        Remove an item from the order.

        :param item_id: Identifier of the item to remove
        """
        order = self.order_repository.get_order()
        order.remove_item(item_id)
        self.order_repository.save_order(order)

    def get_order_items(self) -> list[dict]:
        """
        Retrieve order items formatted for the view.

        :return: List of order items as dictionaries
        """
        return self.order_repository.get_order().to_view_data()

    def get_total(self) -> int:
        """
        Calculate the total price of the order.

        :return: Total amount
        """
        return self.order_repository.get_order().total()

    def get_order_summary(self) -> tuple[list[dict], int]:
        """
        Retrieve both order items and total in one call.

        :return: Tuple of (order_items, total)
        """
        order = self.order_repository.get_order()
        return order.to_view_data(), order.total()

    def place_order(self) -> tuple[list[dict], int]:
        """
        Finalize the order and return a summary.

        Note:
        This method does not persist or clear the order. That is handled separately.

        :return: Tuple of (order_items, total)
        """
        order = self.order_repository.get_order()
        summary_items = order.to_view_data()
        total = order.total()
        return summary_items, total

    def clear_order(self) -> None:
        """
        Clear the current order from the repository.
        """
        self.order_repository.clear_order()

    def is_empty(self) -> bool:
        """
        Check whether the order is empty.

        :return: True if no items are in the order, otherwise False
        """
        return self.order_repository.get_order().is_empty()