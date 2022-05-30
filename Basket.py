class Basket():
    def __init__(self):
        self.Products_in_Basket = []
    def addProduct(self, p):
        self.Products_in_Basket.append(p)
    def buyProduct(self, p):
        self.Products_in_Basket.remove(p)
    