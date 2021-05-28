class Reciept:
    def __init__(self, product, staff, time, quantity, id=None):
        self.product = product
        self.staff = staff
        self.time = time
        self.quantity = quantity
        self.id = id