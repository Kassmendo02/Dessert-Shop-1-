# dessert.py

# This is the main dessert item that others will inherit from
class DessertItem:
    def __init__(self, name=""):
        self.name = name


# Candy is a type of DessertItem
class Candy(DessertItem):
    def __init__(self, name="", candy_weight=0.0, price_per_pound=0.0):
        # Call the parent (DessertItem) constructor to set the name
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound


# Cookie is a type of DessertItem
class Cookie(DessertItem):
    def __init__(self, name="", cookie_quantity=0, price_per_dozen=0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen


# IceCream is a type of DessertItem
class IceCream(DessertItem):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop


# Sundae is a type of IceCream with a topping
class Sundae(IceCream):
    def __init__(
        self,
        name="",
        scoop_count=0,
        price_per_scoop=0.0,
        topping_name="",
        topping_price=0.0,
    ):
        # Initialize the IceCream part of the Sundae
        super().__init__(name, scoop_count, price_per_scoop)
        # Then add the extra Sundae stuff
        self.topping_name = topping_name
        self.topping_price = topping_price

# dessert.py

# ... your existing DessertItem, Candy, Cookie, IceCream, Sundae classes ...


class Order:
    """A list-like container for DessertItem objects."""

    def __init__(self):
        # list of DessertItem objects
        self.order = []

    def add(self, item):
        """Add a single DessertItem to the order."""
        self.order.append(item)

    def __len__(self):
        """Return the number of items in the order."""
        return len(self.order)
