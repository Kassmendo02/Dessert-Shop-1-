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

    while True:
        print("1: Candy")
        print("2: Cookie")
        print("3: Ice Cream")
        print("4: Sundae")
        print()

        choice = input("What would you like to add to the order? (1-4, Enter for done): ").strip()

        if choice == "":
            break

        if choice == "1":
            order.add(shop.user_prompt_candy())
        elif choice == "2":
            order.add(shop.user_prompt_cookie())
        elif choice == "3":
            order.add(shop.user_prompt_icecream())
        elif choice == "4":
            order.add(shop.user_prompt_sundae())
        else:
            print("Invalid choice.")
        print()

    # Build the receipt
    data = []

    for item in order.order:
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        data.append([item.name, f"${cost:.2f}", f"${tax:.2f}"])

    subtotal = order.order_cost()
    total_tax = order.order_tax()
    total = subtotal + total_tax

    if len(order) > 0:
        data.append(["----------------", "--------", "--------"])
        data.append(["Order Subtotals", f"${subtotal:.2f}", f"${total_tax:.2f}"])
        data.append(["Order Total", f"${total:.2f}", ""])
        data.append(["Total Items in the order:", len(order), ""])
    else:
        data.append(["(No items in order)", "", ""])

    print(tabulate(data, headers=["Name", "Cost", "Tax"], tablefmt="fsql"))


if __name__ == "__main__":
    main()
