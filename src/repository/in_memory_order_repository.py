from repository.order_repository import OrderRepository


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._order = []
        self._tip_percentage = 0.0

    def get_order(self):
        return self._order

    def get_tip_percentage(self):
        return self._tip_percentage

    def set_tip_percentage(self, tip_percentage):
        self._tip_percentage = tip_percentage

    def clear_order(self):
        self._order.clear()
        self._tip_percentage = 0.0