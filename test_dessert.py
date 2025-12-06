from dessert import Candy

# DessertItem tests (using Candy as the concrete subclass)

def test_dessertitem_name_default():
    c = Candy()
    assert c.name == ""

def test_dessertitem_name_provided():
    c = Candy("Candy Corn", 1.5, 0.25)
    assert c.name == "Candy Corn"

def test_dessertitem_name_updated():
    c = Candy("Foo", 1.0, 0.10)
    c.name = "Bar"
    assert c.name == "Bar"

def test_dessertitem_tax_percent_default():
    c = Candy()
    assert c.tax_percent == 7.25

def test_dessertitem_tax_percent_updated():
    c = Candy("Candy Corn", 1.5, 0.25)
    c.tax_percent = 10.0
    assert c.tax_percent == 10.0

def test_dessertitem_calculate_tax_uses_tax_percent():
    # Candy Corn example: 1.5 * 0.25 = 0.38 cost, tax 7.25% → 0.03
    c = Candy("Candy Corn", 1.5, 0.25)
    assert c.calculate_cost() == 0.38
    assert c.calculate_tax() == 0.03


# ------------------------------------------------------------
# PART 9 — Relational Operator Tests
# ------------------------------------------------------------
def test_dessertitem_relational_operators():
    a = Candy("A", 1.0, 1.00)   # cost = 1.00
    b = Candy("B", 2.0, 1.00)   # cost = 2.00

    # Test ALL relational operators once:
    assert a < b
    assert a <= b
    assert b > a
    assert b >= a
    assert a != b
    assert a == a
