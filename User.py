from Basket import Basket
class User(Basket):
    def __init__(self, login, password):
        super().__init__()
        self.login = login
        self.password = password
