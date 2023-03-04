class Customer:
    def __init__(self, customer_number, name):
        self.customer_number = customer_number
        self.name = name

class Product:
    def __init__(self, product_number, product_description, product_cost):
        self.product_number = product_number
        self.product_description = product_description
        self.product_cost = product_cost

class Order:
    def __init__(self, order_number, customer_number):
        self.order_number = order_number
        self.customer_number = customer_number


class OrderLine:
    def __init__(self, line_number, order_number, product_number, product_cost, quantity):
        self.line_number = line_number
        self.order_number = order_number
        self.product_number = product_number
        self.product_cost = product_cost
        self.quantity = quantity
        self.extended_cost = product_cost * quantity

    def print_details(self):

        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(self.line_number, self.product_number, f"${self.product_cost:,.2f}", self.quantity,f"${self.extended_cost:,.2f}"))


class Main:
    def __init__(self):
        # Creating customer object
        customer1 = Customer(18, "virat Kohli")

        # Creating product object
        product1 = Product(1, "Cricket Bat", 1000.99)

        product2 = Product(2, "Cricket Ball", 500.89)

        # Creating order object
        order = Order(101, customer1.customer_number)

        # Creating order line object
        order_line1 = OrderLine(101, order.order_number, product1.product_number, product1.product_cost, 2)
        order_line2 = OrderLine(201, order.order_number, product2.product_number, product2.product_cost, 10)
        print("--------------------------------------------------------------------------------------------------")
        print("\t Customer_Number : {:<15} Customer_Name: {:<15}".format(customer1.customer_number, customer1.name))

        print("\t Order_Number : {0}".format(order.order_number))

        print("--------------------------------------------------------------------------------------------------")

        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("line_number", "product_number",
                                                          f"product_cost", "quantity",
                                                          f"extended_cost"))
        print("--------------------------------------------------------------------------------------------------")
        order_line1.print_details()
        order_line2.print_details()

        list_of_order_lines = []
        list_of_order_lines.append(order_line1)
        list_of_order_lines.append(order_line2)
        grand_total = 0
        for cost in list_of_order_lines:
            grand_total += cost.extended_cost
        print("--------------------------------------------------------------------------------------------------")
        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("", "",
                                                          "", "grand-total",
                                                          f"${grand_total:,.2f}"))
        print("--------------------------------------------------------------------------------------------------")

        # Printing details of order line object

if __name__ == "__main__":
    main = Main()
