from repository.order_repository import OrderRepository


class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def add_item(self, item_data: dict) -> None:
        order = self.order_repository.get_order()

        item_id = item_data.get("item_id") or item_data.get("name_key") or item_data["name"]
        name_key = item_data.get("name_key")
        name = item_data["name"]
        price = item_data["price"]

        order.add_item(item_id=item_id, name=name, price=price, name_key=name_key)
        self.order_repository.save_order(order)

    def change_quantity(self, item_id: str, delta: int) -> None:
        order = self.order_repository.get_order()
        order.change_quantity(item_id, delta)
        self.order_repository.save_order(order)

    def remove_item(self, item_id: str) -> None:
        order = self.order_repository.get_order()
        order.remove_item(item_id)
        self.order_repository.save_order(order)

    def get_order_items(self) -> list[dict]:
        return self.order_repository.get_order().to_view_data()

    def get_total(self) -> int:
        return self.order_repository.get_order().total()

    def get_order_summary(self) -> tuple[list[dict], int]:
        order = self.order_repository.get_order()
        return order.to_view_data(), order.total()

    def place_order(self) -> tuple[list[dict], int]:
        order = self.order_repository.get_order()
        summary_items = order.to_view_data()
        total = order.total()
        return summary_items, total

    def clear_order(self) -> None:
        self.order_repository.clear_order()

    def is_empty(self) -> bool:
        return self.order_repository.get_order().is_empty()