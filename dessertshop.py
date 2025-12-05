from tabulate import tabulate
from dessert import Candy, Cookie, IceCream, Sundae, Order


class DessertShop:

    def user_prompt_candy(self):
        name = input("Enter name of candy: ")

        weight = input("Enter weight (lbs): ")
        while not weight.replace(".", "", 1).isdigit():
            weight = input("Please enter a valid number for weight: ")
        weight = float(weight)

        price = input("Enter price per pound: ")
        while not price.replace(".", "", 1).isdigit():
            price = input("Please enter a valid number for price: ")
        price = float(price)

        return Candy(name, weight, price)

    def user_prompt_cookie(self):
        name = input("Enter name of cookie: ")

        qty = input("Enter the number of cookies: ")
        while not qty.isdigit():
            qty = input("Please enter a whole number for quantity: ")
        qty = int(qty)

        price = input("Enter the price per dozen: ")
        while not price.replace(".", "", 1).isdigit():
            price = input("Please enter a valid number for price: ")
        price = float(price)

        return Cookie(name, qty, price)

    def user_prompt_icecream(self):
        name = input("Enter the type of ice cream: ")

        scoops = input("Enter the number of scoops: ")
        while not scoops.isdigit():
            scoops = input("Please enter a whole number for scoops: ")
        scoops = int(scoops)

        price = input("Enter the price per scoop: ")
        while not price.replace(".", "", 1).isdigit():
            price = input("Please enter a valid number for price: ")
        price = float(price)

        return IceCream(name, scoops, price)

    def user_prompt_sundae(self):
        name = input("Enter the type of ice cream: ")

        scoops = input("Enter the number of scoops: ")
        while not scoops.isdigit():
            scoops = input("Please enter a whole number for scoops: ")
        scoops = int(scoops)

        price = input("Enter the price per scoop: ")
        while not price.replace(".", "", 1).isdigit():
            price = input("Please enter a valid number for price: ")
        price = float(price)

        topping_name = input("Enter the topping: ")

        topping_price = input("Enter the price for the topping: ")
        while not topping_price.replace(".", "", 1).isdigit():
            topping_price = input("Please enter a valid number for topping price: ")
        topping_price = float(topping_price)

        return Sundae(name, scoops, price, topping_name, topping_price)


def main():

    shop = DessertShop()
    order = Order()

    done: bool = False

    prompt = '\n'.join([
        '\n',
        '1: Candy',
        '2: Cookie',
        '3: Ice Cream',
        '4: Sundae',
        '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])

    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case _:
                print("Invalid response: Please enter 1–4 or press Enter.")

    print()
    print(tabulate(order.to_list(), tablefmt="fsql"))

