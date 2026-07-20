
"""
Exercise G starter — a SalesTracker class that's already working, with
two methods left as TODOs for the candidate to implement. Give the
candidate ONLY this file.

Run with: python starter.py
(It'll run fine until it hits the two NotImplementedError calls at the
bottom — that's expected; those are what the candidate needs to build.)
"""


class SalesTracker:
    """Tracks orders across customers so the sales team can see revenue
    over a date range and who the top customer is."""

    def __init__(self):
        self.orders = []  # each: {"customer": str, "amount": float, "date": "YYYY-MM-DD"}

    def add_order(self, customer, amount, date):
        self.orders.append({"customer": customer, "amount": amount, "date": date})

    def order_count(self):
        return len(self.orders)

    def total_revenue(self, start_date=None, end_date=None):
        """TODO: implement this.

        Return the sum of `amount` across all orders. If `start_date`
        and/or `end_date` are given (as "YYYY-MM-DD" strings), only
        include orders whose date falls within that range, inclusive on
        both ends. If there are no matching orders, return 0.
        """
        raise NotImplementedError

    def top_customer(self):
        """TODO: implement this.

        Return a (customer, total_spent) tuple for whichever customer has
        the highest total spend across ALL their orders (not just their
        single biggest order). If there are no orders at all, return
        None.
        """
        raise NotImplementedError


if __name__ == "__main__":
    tracker = SalesTracker()
    tracker.add_order("Acme Corp", 500, "2026-01-05")
    tracker.add_order("Acme Corp", 300, "2026-02-10")
    tracker.add_order("Globex", 900, "2026-01-20")
    tracker.add_order("Initech", 150, "2026-03-01")
    tracker.add_order("Globex", 200, "2026-03-15")

    print(f"Order count: {tracker.order_count()}")

    # Once implemented, this should print 2050 (sum of all order amounts)
    print(f"Total revenue: {tracker.total_revenue()}")

    # Once implemented, this should print only January's orders: 500 + 900 = 1400
    print(f"January revenue: {tracker.total_revenue(start_date='2026-01-01', end_date='2026-01-31')}")

    # Once implemented: Acme Corp spent 800 total (500+300), Globex spent
    # 1100 total (900+200) -> Globex is the top customer, not Acme (even
    # though no single Acme order matches Globex's biggest single order).
    print(f"Top customer: {tracker.top_customer()}")
