from model.order_item import OrderItem


class Order:
    def __init__(self):
        self.items: list[OrderItem] = []

    def find_item(self, item_id: str) -> OrderItem | None:
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def add_item(self, item_id: str, name: str, price: int) -> None:
        existing_item = self.find_item(item_id)
        if existing_item:
            existing_item.increase()
        else:
            self.items.append(OrderItem(item_id=item_id, name=name, price=price, quantity=1))

    def change_quantity(self, item_id: str, delta: int) -> None:
        item = self.find_item(item_id)
        if not item:
            return

        if delta > 0:
            item.increase(delta)
        elif delta < 0:
            item.decrease(abs(delta))

        if item.quantity <= 0:
            self.remove_item(item_id)

    def remove_item(self, item_id: str) -> None:
        self.items = [item for item in self.items if item.item_id != item_id]

    def clear(self) -> None:
        self.items.clear()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def total(self) -> int:
        return sum(item.subtotal() for item in self.items)

    def to_view_data(self) -> list[dict]:
        return [
            {
                "item_id": item.item_id,
                "name": item.name,
                "price": item.price,
                "quantity": item.quantity,
            }
            for item in self.items
        ]