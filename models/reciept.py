class Reciept:
    def __init__(self, product, staff, time_stamp, quantity, id=None):
        self.product = product
        self.staff = staff
        self.time_stamp = time_stamp
        self.quantity = quantity
        self.id = id