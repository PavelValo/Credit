from Category import Category
from Product import Product

def generateCategories():
    file = open("build materials.txt", 'r', encoding='utf8')
    line = file.readline()
    Categ = []       #набор каталогов
    while line != "":   #конец файла или нет
        line = line[0:len(line) - 1]
        newCat = Category(line)     #создать каталог
        line = file.readline()
        line = line[0:len(line) - 1]
        while line != "":
            tmp = line.split(", ")
            newProd = Product(tmp[0], float(tmp[1]), int(tmp[2]), float(tmp[3]))
            newCat.addProduct(newProd)      #добавить товар к каталогу
            line = file.readline()
            line = line[0:len(line) - 1]
        Categ.append(newCat)    #добавление каталога к набору каталогов
        line = file.readline()
    file.close()
    return Categ
