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


# --------------------------------------------------------
# PART 9 — Test Order.sort() sorts by ascending cost
# --------------------------------------------------------

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
