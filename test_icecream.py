from dessert import IceCream


def test_icecream_defaults():
    ic = IceCream()
    assert ic.name == ""
    assert ic.scoop_count == 0
    assert ic.price_per_scoop == 0


def test_icecream_provided_values():
    ic = IceCream("Pistachio", 2, 0.79)
    assert ic.name == "Pistachio"
    assert ic.scoop_count == 2
    assert ic.price_per_scoop == 0.79


def test_icecream_updated_values():
    ic = IceCream("Vanilla", 1, 0.89)
    ic.scoop_count = 3
    ic.price_per_scoop = 1.00
    assert ic.scoop_count == 3
    assert ic.price_per_scoop == 1.00


def test_icecream_calculate_cost():
    ic = IceCream("Pistachio", 2, 0.79)
    assert ic.calculate_cost() == 1.58


def test_icecream_calculate_tax():
    ic = IceCream("Pistachio", 2, 0.79)
    assert ic.calculate_tax() == 0.11


def test_icecream_packaging():
    ic = IceCream("Pistachio", 2, 0.79)
    assert ic.packaging == "Bowl"
