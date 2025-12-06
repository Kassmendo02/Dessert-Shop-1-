# dessert.py
from abc import ABC, abstractmethod
from packaging import Packaging


# ------------------------------
# DessertItem base class
# ------------------------------
class DessertItem(ABC, Packaging):
    def __init__(self, name="", tax_percent=7.25):
        self.name = name
        self.tax_percent = tax_percent
        self.packaging = None   # will be set in each subclass

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        cost = self.calculate_cost()
        return round(cost * (self.tax_percent / 100), 2)


# ------------------------------
# Candy
# ------------------------------
class Candy(DessertItem):
    def __init__(self, name="", candy_weight=0.0, price_per_pound=0.0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"

    def calculate_cost(self):
        return round(self.candy_weight * self.price_per_pound, 2)

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return (
            f"{self.name} ({self.packaging})\n"
            f" -   {self.candy_weight} lbs. @ ${self.price_per_pound}/lb:, "
            f"${cost:.2f}, [Tax: ${tax:.2f}]"
        )


# ------------------------------
# Cookie
# ------------------------------
class Cookie(DessertItem):
    def __init__(self, name="", cookie_quantity=0, price_per_dozen=0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"

    def calculate_cost(self):
        dozens = self.cookie_quantity / 12
        return round(dozens * self.price_per_dozen, 2)

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return (
            f"{self.name} Cookies ({self.packaging})\n"
            f" -   {self.cookie_quantity} cookies. @ ${self.price_per_dozen}/dozen:, "
            f"${cost:.2f}, [Tax: ${tax:.2f}]"
        )


# ------------------------------
# Ice Cream
# ------------------------------
class IceCream(DessertItem):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"

    def calculate_cost(self):
        return round(self.scoop_count * self.price_per_scoop, 2)

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return (
            f"{self.name} Ice Cream ({self.packaging})\n"
            f" -   {self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop:, "
            f"${cost:.2f}, [Tax: ${tax:.2f}]"
        )


# ------------------------------
# Sundae
# ------------------------------
class Sundae(IceCream):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0,
                 topping_name="", topping_price=0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"

    def calculate_cost(self):
        base_cost = self.scoop_count * self.price_per_scoop
        total_cost = base_cost + self.topping_price
        return round(total_cost, 2)

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return (
            f"{self.topping_name} {self.name} Sundae ({self.packaging})\n"
            f" -   {self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop\n"
            f" -   {self.topping_name} topping @ ${self.topping_price}:, "
            f"${cost:.2f}, [Tax: ${tax:.2f}]"
        )


# Order class
from payment import PayType, Payable

class Order(Payable):
    def __init__(self):
        self.order = []                # list of DessertItem objects
        self.pay_type: PayType = "CASH"  # default payment type

    def add(self, item):
        self.order.append(item)

    def __len__(self):
        return len(self.order)

    # -------------------------
    # Receipt formatting
    # -------------------------
    def __str__(self):
        lines = []

        # Print each dessert item using its __str__()
        for item in self.order:
            lines.append(str(item))

        subtotal = self.order_cost()
        tax_total = self.order_tax()
        total = subtotal + tax_total

        lines.append(f"Total number of items in order: {len(self.order)}")
        lines.append(f"Order Subtotals: ${subtotal:.2f}, [Tax: ${tax_total:.2f}]")
        lines.append(f"Order Total: ${total:.2f}")
        lines.append("Paid with " + self.pay_type)

        return "\n".join(lines)

    # -------------------------
    # Convert to list method (unchanged)
    # -------------------------
    def to_list(self):
        rows = []
        for line in str(self).split("\n"):
            rows.append(line.split(","))
        return rows

    # -------------------------
    # Order totals
    # -------------------------
    def order_cost(self):
        return round(sum(item.calculate_cost() for item in self.order), 2)

    def order_tax(self):
        return round(sum(item.calculate_tax() for item in self.order), 2)

    # -------------------------
    # Payment interface methods (Part 8 requirement)
    # -------------------------
    def get_pay_type(self) -> PayType:
        if self.pay_type not in ["CASH", "CARD", "PHONE"]:
            raise ValueError("Invalid payment type stored in Order.")
        return self.pay_type

    def set_pay_type(self, payment_method: PayType) -> None:
        if payment_method not in ["CASH", "CARD", "PHONE"]:
            raise ValueError("Invalid payment type.")
        self.pay_type = payment_method
