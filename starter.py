"""
Exercise D starter — process a CSV of orders and compute revenue totals.
"""
import csv

def load_orders(path):
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def total_revenue(orders):
    total = 0
    for order in orders:
        total += float(order["amount"])
    return total


if __name__ == "__main__":
    orders = load_orders("orders.csv")
    print(f"Loaded {len(orders)} orders")
    print(f"Total revenue: {total_revenue(orders)}")
