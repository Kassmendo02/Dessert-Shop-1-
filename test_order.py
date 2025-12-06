import pytest
from dessert import Order

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
