from model.order import Order
from repository.order_repository import OrderRepository


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._current_order = Order()
        self._tip_percentage = 0.0

    def get_order(self):
        return self._current_order

    def save_order(self, order):
        self._current_order = order

    def clear_order(self):
        self._current_order = Order()

    def get_tip_percentage(self):
        return self._tip_percentage

    def set_tip_percentage(self, tip_percentage):
        self._tip_percentage = tip_percentage