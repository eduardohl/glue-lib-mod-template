from dataclasses import dataclass


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def show_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


@dataclass
class InventoryItem:
    name: str
    owner: Person
    unit_price: float = 1.0
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
