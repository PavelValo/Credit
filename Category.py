class Category():
    def __init__(self, name):
        self.name = name
        self.ProductArr = []
    def addProduct(self, p):
        self.ProductArr.append(p)
    def removeProduct(self, p):
        self.ProductArr.remove(p)