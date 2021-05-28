class Product:
    def __init__(self, name, description, stock_quantity, buy_price, sell_price, manufacturer, id=None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buy_price = buy_price
        self. sell_price = sell_price
        self.manufacturer = manufacturer
        self.id = id