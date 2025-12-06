import pytest
from dessert import Order, Candy


# --- VALID PAYMENT TYPES ---

def test_set_cash():
    o = Order()
    o.set_pay_type("CASH")
    assert o.get_pay_type() == "CASH"


def test_set_card():
    o = Order()
    o.set_pay_type("CARD")
    assert o.get_pay_type() == "CARD"


def test_set_phone():
    o = Order()
    o.set_pay_type("PHONE")
    assert o.get_pay_type() == "PHONE"


# --- INVALID PAYMENT SETTING ---

def test_set_invalid_payment():
    o = Order()
    with pytest.raises(ValueError):
        o.set_pay_type("APPLEPAY")


# --- INVALID GET (BAD INTERNAL VALUE) ---

def test_get_invalid_payment():
    o = Order()
    o.pay_type = "BADVALUE"   # force an illegal stored value
    with pytest.raises(ValueError):
        o.get_pay_type()


def test_order_sort():
    o = Order()

    # Create desserts with different prices
    cheap = Candy("Cheap", 1, 1.00)     # cost = 1.00
    mid = Candy("Mid", 2, 1.00)         # cost = 2.00
    expensive = Candy("Expensive", 3, 1.00)  # cost = 3.00

    # Add in a mixed order
    o.add(mid)
    o.add(expensive)
    o.add(cheap)

    # Apply sorting
    o.sort()

    # Check ascending order
    assert o.order[0] == cheap
    assert o.order[1] == mid
    assert o.order[2] == expensive


def test_order_iterator():
    o = Order()

    # Add items in known order
    c1 = Candy("A", 1, 1.00)
    c2 = Candy("B", 2, 1.00)
    c3 = Candy("C", 3, 1.00)

    o.add(c1)
    o.add(c2)
    o.add(c3)

    it = iter(o)

    # Check each value returned in order
    assert next(it) is c1
    assert next(it) is c2
    assert next(it) is c3

    # After last element, StopIteration should be raised
    try:
        next(it)
        assert False     # should NOT reach this line
    except StopIteration:
        assert True
