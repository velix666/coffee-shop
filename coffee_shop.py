from abc import ABC, abstractmethod


class Drink(ABC):
    def __init__(self, name: str, price: float, volume: int):
        self.name = name
        self.price = price
        self.__volume = volume
        self._sold = 0

    @property
    def volume(self) -> int:
        return self.__volume

    @property
    def sold(self) -> int:
        return self._sold

    def sell(self, cups: int = 1) -> float:
        self._sold += cups
        return self.price * cups

    @abstractmethod
    def describe(self) -> str:
        ...


class Coffee(Drink):
    def __init__(self, name, price, volume, beans: str):
        super().__init__(name, price, volume)
        self.beans = beans

    def describe(self) -> str:
        return f"{self.name} ({self.beans}), {self.volume} мл — {self.price}₽"


class Tea(Drink):
    def __init__(self, name, price, volume, kind: str):
        super().__init__(name, price, volume)
        self.kind = kind

    def describe(self) -> str:
        return f"{self.name} ({self.kind}), {self.volume} мл — {self.price}₽"


class Order:
    def __init__(self):
        self.items = []

    def add(self, drink: Drink, cups: int = 1):
        self.items.append((drink, cups))


class ReceiptPrinter:
    def print_receipt(self, order: Order):
        total = 0
        print("--- Чек ---")
        for drink, cups in order.items:
            cost = drink.sell(cups)
            total += cost
            print(f"{drink.describe()} x{cups} = {cost}₽")
        print(f"Итого: {total}₽")


class Discount:
    def apply(self, total: float) -> float:
        return total


class HappyHourDiscount(Discount):
    def apply(self, total: float) -> float:
        return total * 0.7


def sell_all(drinks: list):
    for d in drinks:
        print(d.describe())


if __name__ == "__main__":
    latte = Coffee("Латте", 250, 300, "арабика")
    earl = Tea("Эрл Грей", 150, 400, "чёрный")

    order = Order()
    order.add(latte, 2)
    order.add(earl, 1)

    printer = ReceiptPrinter()
    printer.print_receipt(order)

    print(f"\nПродано латте: {latte.sold} шт.")

    print("\nМеню:")
    sell_all([latte, earl])

    discount = HappyHourDiscount()
    print(f"\nСо скидкой 30%: {discount.apply(650)}₽")