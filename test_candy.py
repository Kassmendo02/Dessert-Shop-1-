from dessert import Candy


def test_candy_defaults():
    c = Candy()
    assert c.name == ""
    assert c.candy_weight == 0
    assert c.price_per_pound == 0


def test_candy_provided_values():
    c = Candy("Candy Corn", 1.5, 0.25)
    assert c.name == "Candy Corn"
    assert c.candy_weight == 1.5
    assert c.price_per_pound == 0.25


def test_candy_updated_values():
    c = Candy("Gummy Bears", 1.0, 0.30)
    c.candy_weight = 2.0
    c.price_per_pound = 0.40
    assert c.candy_weight == 2.0
    assert c.price_per_pound == 0.40


def test_candy_calculate_cost():
    c = Candy("Candy Corn", 1.5, 0.25)
    assert c.calculate_cost() == 0.38


def test_candy_calculate_tax():
    c = Candy("Candy Corn", 1.5, 0.25)
    assert c.calculate_tax() == 0.03


def test_candy_packaging():
    c = Candy("Candy Corn", 1.5, 0.25)
    assert c.packaging == "Bag"
