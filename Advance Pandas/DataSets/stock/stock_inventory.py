import json
products = []


def addProduct(name, price, qty):
    products.append({"name": name, "price": price, "qty": qty})


def showProducts():
    show_option_menu("Display Products")
    if len(products) > 0:
        for p in products:
            print(
                f"Name: {p['name']} - Price: {p['price']} - Quantity: {p['qty']}")
    else:
        print("No product found!")


def removeProduct(name):
    index = getProductIndex(name)
    products.pop(index)

def getProductIndex(name):
    for p in products:
        if p["name"].lower() == name.lower():
            return products.index(p)
            
def incrementQuantity(name, incQty):
    index = getProductIndex(name)
    products[index]["qty"] += incQty

def decrementQuantity(name, decQty):
    index = getProductIndex(name)    
    products[index]["qty"] -= decQty

    if products[index]["qty"] < 1:
        products[index]["qty"] = 0

def renameProduct(name, newName):
    index = getProductIndex(name)
    products[index]["name"] = newName

def changePrice(name, price):
    index = getProductIndex(name)
    products[index]["price"] = price

def show_option_menu(title):
    print(title)
    print("-----------------------------------------------")

def take_add_product_input():
    show_option_menu("Add Product")
    ui = input("Product should have Name, price, quantity (eg: lays, 5, 10) : ")
    prd = ui.strip().split(',')
    addProduct(prd[0].strip(),float(prd[1].strip()),int(prd[2].strip()))

def take_remove_product_input():
    show_option_menu("Remove Product")
    ui = input("Type product name: ")
    removeProduct(ui.strip())

def take_rename_product_input():
    show_option_menu("Rename Product")
    ui = input("Type product name and new name (eg: lays, Kurleez): ")
    prd = ui.strip().split(',')
    renameProduct(prd[0].strip(), prd[1].strip())

def take_change_price_input():
    show_option_menu("Change Price")
    ui = input("Type product name and new price (eg: lays, 15): ")
    prd = ui.strip().split(',')
    changePrice(prd[0].strip(),float(prd[1].strip()))

def take_inc_qty_input():
    show_option_menu("Increment Quantity")
    ui = input("Type product name and quantity (eg: lays, 150): ")
    prd = ui.strip().split(',')
    incrementQuantity(prd[0].strip(),int(prd[1].strip()))

def take_dec_qty_input():
    show_option_menu("Decrement Quantity")
    ui = input("Type product name and quantity (eg: lays, 15): ")
    prd = ui.strip().split(',')
    decrementQuantity(prd[0].strip(),int(prd[1].strip()))

def saveproduct():
    data=json.dumps(products)
#     print(data)
    with open("store_db.text","w") as file:
        file.write(data)

def loadProduct():
    data=json.loads(products)
    with open("store_db.text","w") as file:
        file.read(data)


addProduct('test',1,1)
showProducts()
saveproduct()
loadProduct()





#     with open('config.json') as f:
#         data = json.loads(f)

#     v1, v2 = data['x'], data['y']
#     multiplier = eval(data['func'])
#     print(multiplier(v1, v2))




