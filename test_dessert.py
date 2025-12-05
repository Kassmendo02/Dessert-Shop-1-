from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

# ----------------------------
# DessertItem Tests
# ----------------------------
def test_dessertitem_defaults():
    d = DessertItem()
    assert d.name == ""

def test_dessertitem_provided_values():
    d = DessertItem("Brownie")
    assert d.name == "Brownie"

def test_dessertitem_updated_values():
    d = DessertItem("Pie")
    d.name = "Apple Pie"
    assert d.name == "Apple Pie"


# ----------------------------
# Candy Tests
# ----------------------------
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


# ----------------------------
# Cookie Tests
# ----------------------------
def test_cookie_defaults():
    ck = Cookie()
    assert ck.name == ""
    assert ck.number_of_cookies == 0
    assert ck.price_per_dozen == 0

def test_cookie_provided_values():
    ck = Cookie("Chocolate Chip", 6, 3.99)
    assert ck.name == "Chocolate Chip"
    assert ck.number_of_cookies == 6
    assert ck.price_per_dozen == 3.99

def test_cookie_updated_values():
    ck = Cookie("Oatmeal", 2, 3.45)
    ck.number_of_cookies = 12
    ck.price_per_dozen = 4.00
    assert ck.number_of_cookies == 12
    assert ck.price_per_dozen == 4.00


# ----------------------------
# IceCream Tests
# ----------------------------
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


# ----------------------------
# Sundae Tests
# ----------------------------
def test_sundae_defaults():
    s = Sundae()
    assert s.name == ""
    assert s.scoop_count == 0
    assert s.price_per_scoop == 0
    assert s.topping_name == ""
    assert s.topping_price == 0

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
