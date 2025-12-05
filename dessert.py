# dessert.py

from abc import ABC, abstractmethod


# This is the main dessert item that others will inherit from
class DessertItem(ABC):
    def __init__(self, name: str = "", tax_percent: float = 7.25):
        self.name = name
        self.tax_percent = tax_percent

    @abstractmethod
    def calculate_cost(self) -> float:
        """Return the cost of this dessert item."""
        pass

    def calculate_tax(self) -> float:
        """Return the tax for this dessert item, rounded to 2 decimals."""
        cost = self.calculate_cost()
        tax = cost * (self.tax_percent / 100)
        return round(tax, 2)


# Candy is a type of DessertItem
class Candy(DessertItem):
    def __init__(self, name: str = "", candy_weight: float = 0.0, price_per_pound: float = 0.0):
        # Call the parent (DessertItem) constructor to set the name
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self) -> float:
        cost = self.candy_weight * self.price_per_pound
        return round(cost, 2)


# Cookie is a type of DessertItem
class Cookie(DessertItem):
    def __init__(self, name: str = "", cookie_quantity: int = 0, price_per_dozen: float = 0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self) -> float:
        dozens = self.cookie_quantity / 12
        cost = dozens * self.price_per_dozen
        return round(cost, 2)


# IceCream is a type of DessertItem
class IceCream(DessertItem):
    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self) -> float:
        cost = self.scoop_count * self.price_per_scoop
        return round(cost, 2)


# Sundae is a type of IceCream with a topping
class Sundae(IceCream):
    def __init__(
        self,
        name: str = "",
        scoop_count: int = 0,
        price_per_scoop: float = 0.0,
        topping_name: str = "",
        topping_price: float = 0.0,
    ):
        # Initialize the IceCream part of the Sundae
        super().__init__(name, scoop_count, price_per_scoop)
        # Then add the extra Sundae stuff
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self) -> float:
        ice_cream_cost = super().calculate_cost()
        cost = ice_cream_cost + self.topping_price
        return round(cost, 2)


class Order:
    """A list-like container for DessertItem objects."""

    def __init__(self):
        # list of DessertItem objects
        self.order = []

    def add(self, item: DessertItem):
        """Add a single DessertItem to the order."""
        self.order.append(item)

    def __len__(self):
        """Return the number of items in the order."""
        return len(self.order)

    def order_cost(self) -> float:
        """Return total cost of all items in the order."""
        total = 0.0
        for item in self.order:
            total += item.calculate_cost()
        return round(total, 2)

    def order_tax(self) -> float:
        """Return total tax of all items in the order."""
        total_tax = 0.0
        for item in self.order:
            total_tax += item.calculate_tax()
        return round(total_tax, 2)
