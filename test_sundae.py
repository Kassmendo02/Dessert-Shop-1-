from dessert import Sundae


def test_sundae_defaults():
    s = Sundae()
    assert s.name == ""
    assert s.scoop_count == 0
    assert s.price_per_scoop == 0.0
    assert s.topping_name == ""
    assert s.topping_price == 0.0


def test_sundae_provided_values():
    s = Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29)
    assert s.name == "Vanilla"
    assert s.scoop_count == 3
    assert s.price_per_scoop == 0.69
    assert s.topping_name == "Hot Fudge"
    assert s.topping_price == 1.29


def test_sundae_updated_values():
    s = Sundae("Chocolate", 2, 0.75, "Caramel", 1.00)
    s.topping_name = "Sprinkles"
    s.topping_price = 1.50
    assert s.topping_name == "Sprinkles"
    assert s.topping_price == 1.50


def test_sundae_calculate_cost():
    s = Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29)
    # 3 * 0.69 = 2.07; + 1.29 = 3.36
    assert s.calculate_cost() == 3.36


def test_sundae_calculate_tax():
    s = Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29)
    assert s.calculate_tax() == 0.24


def test_sundae_packaging():
    s = Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29)
    assert s.packaging == "Boat"
