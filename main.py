from Product import Product
from User import User
from generateCategories import generateCategories

# генератор данных
Categ = generateCategories()

# аутентификация пользователя
myUser = User("Павел", "Вало")

login = input("Введите ваш логин:")
password = input("Введите ваш пароль:")
while not (login == myUser.login and password == myUser.password):
    print("\nВаш логин или пароль не правильный. Еще раз попробуйте\n")
    login = input("Введите ваш логин:")
    password = input("Введите ваш пароль:")

# просмотр каталога товаров
print("\nЭто наш список каталогов товаров\n")
for Cat in Categ:
    print(Cat.name)

# выбор каталога
print("\nВыберите желаемый каталог!\n")
flag = False
while not flag:
    tmp = input()
    for Cat in Categ:
        if Cat.name == tmp:
            myCateg = Cat
            flag = True
            break
    if not flag:
        print("\nНеправильное название каталога. Еще раз введите желаемый каталог\n")

# просмтор списка товаров выбранного каталога
for Prod1 in myCateg.ProductArr:
    print(f"{Prod1.name}, цена: {Prod1.price}рб, в наличии {Prod1.amount}шт, рейтинг: {Prod1.rating}")

# выбор товара
print("\nВыберите желаемый товар\nВведите название товара\n")
flag = False
while not flag:
    tmp = input()
    for Prod2 in myCateg.ProductArr:
        if Prod2.name == tmp:
            myProduct = Prod2
            flag = True
            break
    if not flag:
        print("\nНеправильное название товара. Еще раз введите желаемый товар\n")

# выбор количества
print(f"\nХороший выбор!!!\nТеперь введите желаемое количество товара\n!Учитывайте, что в наличии {myProduct.amount}шт")
myAmount = int(input())

# изменить остаток товар в складе
myCateg.removeProduct(myProduct)
tmpProduct = Product(myProduct.name, myProduct.price, myProduct.amount-myAmount, myProduct.rating)
myCateg.addProduct(tmpProduct)
# добавить в корзину
tmpProduct = Product(myProduct.name, myProduct.price, myAmount, myProduct.rating)
myUser.addProduct(tmpProduct)
print(f"товар: {tmp},   {myAmount} штук добавлено в корзину ")
# купить товар
myUser.buyProduct(tmpProduct)
print(f"товар: {tmp},   {myAmount} штук куплено")
print("Спасибо за покупку!")