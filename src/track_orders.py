from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        orders = []
        for order in self.orders:
            if order[0] == customer:
                orders.append(order[1])

        return Counter(orders).most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        customer_orders = set()
        others_orders = set()
        for other_customer in self.orders:
            if other_customer[0] == customer:
                customer_orders.add(other_customer[1])
            else:
                others_orders.add(other_customer[1])

        return others_orders - customer_orders

    def get_days_never_visited_per_customer(self, customer):
        customer_days = set()
        other_days = set()
        for other_customer in self.orders:
            if other_customer[0] == customer:
                customer_days.add(other_customer[2])
            else:
                other_days.add(other_customer[2])

        return other_days - customer_days

    def get_busiest_day(self):
        days = []
        for customers in self.orders:
            days.append(customers[2])

        return Counter(days).most_common()[0][0]

    def get_least_busy_day(self):
        days = []
        for customers in self.orders:
            days.append(customers[2])

        return Counter(days).most_common()[-1][0]
