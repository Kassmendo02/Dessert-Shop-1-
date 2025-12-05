from dessert import Cookie


def test_cookie_defaults():
    ck = Cookie()
    assert ck.name == ""
    assert ck.cookie_quantity == 0
    assert ck.price_per_dozen == 0


def test_cookie_provided_values():
    ck = Cookie("Chocolate Chip", 6, 3.99)
    assert ck.name == "Chocolate Chip"
    assert ck.cookie_quantity == 6
    assert ck.price_per_dozen == 3.99


def test_cookie_updated_values():
    ck = Cookie("Oatmeal", 2, 3.45)
    ck.cookie_quantity = 12
    ck.price_per_dozen = 4.00
    assert ck.cookie_quantity == 12
    assert ck.price_per_dozen == 4.00


def test_cookie_calculate_cost():
    ck = Cookie("Chocolate Chip", 6, 3.99)
    # 6/12 * 3.99 = 1.995 -> 2.00
    assert ck.calculate_cost() == 2.00


def test_cookie_calculate_tax():
    ck = Cookie("Chocolate Chip", 6, 3.99)
    assert ck.calculate_tax() == 0.14
