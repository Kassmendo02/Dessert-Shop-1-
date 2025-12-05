# dessertshop.py

from tabulate import tabulate
from dessert import Candy, Cookie, IceCream, Sundae, Order


def main():
    # Create a new instance of the Order class
    order = Order()

    # Add the required items to the order
    order.add(Candy("Candy Corn", 1.5, 0.25))            # $0.38
    order.add(Candy("Gummy Bears", 0.25, 0.35))          # $0.09
    order.add(Cookie("Chocolate Chip", 6, 3.99))         # $2.00
    order.add(IceCream("Pistachio", 2, 0.79))            # $1.58
    order.add(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))  # $3.36
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))         # $0.57

    # Build data rows for the receipt
    data = []

    for item in order.order:
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        data.append(
            [
                item.name,
                f"${cost:.2f}",
                f"${tax:.2f}",
            ]
        )

    # Add subtotal and totals
    subtotal = order.order_cost()
    total_tax = order.order_tax()
    total = subtotal + total_tax

    data.append(["----------------", "--------", "--------"])
    data.append(["Order Subtotals", f"${subtotal:.2f}", f"${total_tax:.2f}"])
    data.append(["Order Total", f"${total:.2f}", ""])
    data.append(["Total Items in the order:", len(order), ""])

    # Print the receipt
    print(tabulate(data, headers=["Name", "Cost", "Tax"], tablefmt="fsql"))


if __name__ == "__main__":
    main()
