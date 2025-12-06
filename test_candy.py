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
    
def test_candy_can_combine_true():
    c1 = Candy("Gummy Bears", 1.0, 0.25)
    c2 = Candy("Gummy Bears", 2.0, 0.25)
    assert c1.can_combine(c2) is True


def test_candy_can_combine_false_different_price():
    c1 = Candy("Gummy Bears", 1.0, 0.25)
    c2 = Candy("Gummy Bears", 2.0, 0.30)
    assert c1.can_combine(c2) is False


def test_candy_can_combine_false_different_name():
    c1 = Candy("Candy Corn", 1.0, 0.25)
    c2 = Candy("Gummy Bears", 1.0, 0.25)
    assert c1.can_combine(c2) is False


def test_candy_can_combine_false_not_candy():
    c1 = Candy("Gummy Bears", 1.0, 0.25)
    other = "not a candy"
    assert c1.can_combine(other) is False


def test_candy_combine_success():
    c1 = Candy("Gummy Bears", 1.0, 0.25)
    c2 = Candy("Gummy Bears", 2.0, 0.25)
    c1.combine(c2)
    assert c1.candy_weight == 3.0    # weights added
    assert c1.price_per_pound == 0.25


def test_candy_combine_type_error():
    c1 = Candy("Gummy Bears", 1.0, 0.25)
    other = "not candy"
    try:
        c1.combine(other)
        assert False    # should NOT reach this line
    except TypeError:
        assert True
