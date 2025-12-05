from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name="", tax_percent=7.25):
        self.name = name
        self.tax_percent = tax_percent

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return round(self.calculate_cost() * (self.tax_percent / 100), 2)


class Candy(DessertItem):
    def __init__(self, name="", candy_weight=0.0, price_per_pound=0.0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return round(self.candy_weight * self.price_per_pound, 2)

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return (
            f"{self.name}\n"
            f"-    {self.candy_weight} lbs. @ ${self.price_per_pound}/lb:, "
            f"${cost:.2f}, [Tax: ${tax:.2f}]"
        )


class Cookie(DessertItem):
    def __init__(self, name="", cookie_quantity=0, price_per_dozen=0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        dozens = self.cookie_quantity / 12
        return round(dozens * self.price_per_dozen, 2)

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return (
            f"{self.name} Cookies\n"
            f"-    {self.cookie_quantity} cookies. @ ${self.price_per_dozen}/dozen:, "
            f"${cost:.2f}, [Tax: ${tax:.2f}]"
        )


class IceCream(DessertItem):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        return round(self.scoop_count * self.price_per_scoop, 2)

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return (
            f"{self.name} Ice Cream\n"
            f"-    {self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop:, "
            f"${cost:.2f}, [Tax: ${tax:.2f}]"
        )


class Sundae(IceCream):
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0,
                 topping_name="", topping_price=0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return round(
            (self.scoop_count * self.price_per_scoop) + self.topping_price,
            2
        )

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return (
            f"{self.topping_name} {self.name} Sundae\n"
            f"-    {self.scoop_count} scoops. @ ${self.price_per_scoop}/scoop\n"
            f"-    {self.topping_name} topping @ ${self.topping_price}:, "
            f"${cost:.2f}, [Tax: ${tax:.2f}]"
        )


class Order:
    def __init__(self):
        self.order = []

    def add(self, item):
        self.order.append(item)

    def __len__(self):
        return len(self.order)

    def __str__(self):
        return "\n".join(str(item) for item in self.order)

    def to_list(self):
        return [line.split(",") for line in str(self).split("\n")]

    def order_cost(self):
        return round(sum(item.calculate_cost() for item in self.order), 2)

    def order_tax(self):
        return round(sum(item.calculate_tax() for item in self.order), 2)
