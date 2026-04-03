from dataclasses import dataclass


@dataclass
class OrderItem:
    item_id: str
    name: str
    price: int
    quantity: int = 1

    def increase(self, amount: int = 1) -> None:
        self.quantity += amount

    def decrease(self, amount: int = 1) -> None:
        self.quantity -= amount

    def subtotal(self) -> int:
        return self.price * self.quantity