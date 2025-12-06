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


def test_cookie_packaging():
    ck = Cookie("Chocolate Chip", 6, 3.99)
    assert ck.packaging == "Box"

def test_cookie_can_combine_true():
    ck1 = Cookie("Chocolate Chip", 6, 3.99)
    ck2 = Cookie("Chocolate Chip", 12, 3.99)
    assert ck1.can_combine(ck2) is True


def test_cookie_can_combine_false_different_price():
    ck1 = Cookie("Chocolate Chip", 6, 3.99)
    ck2 = Cookie("Chocolate Chip", 12, 4.99)
    assert ck1.can_combine(ck2) is False


def test_cookie_can_combine_false_different_name():
    ck1 = Cookie("Oatmeal", 6, 3.99)
    ck2 = Cookie("Chocolate Chip", 6, 3.99)
    assert ck1.can_combine(ck2) is False


def test_cookie_can_combine_false_not_cookie():
    ck1 = Cookie("Chocolate Chip", 6, 3.99)
    other = "not a cookie"
    assert ck1.can_combine(other) is False


def test_cookie_combine_success():
    ck1 = Cookie("Chocolate Chip", 6, 3.99)
    ck2 = Cookie("Chocolate Chip", 12, 3.99)
    ck1.combine(ck2)
    assert ck1.cookie_quantity == 18
    assert ck1.price_per_dozen == 3.99


def test_cookie_combine_type_error():
    ck1 = Cookie("Chocolate Chip", 6, 3.99)
    other = 123  # not a Cookie
    try:
        ck1.combine(other)
        assert False     # should NOT reach here
    except TypeError:
        assert True
