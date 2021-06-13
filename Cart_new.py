Products = {}
cart = []


def printOptions1():
    print("1. Add Product")
    print("2. View Product")
    print("3. Add to Cart")
    print("4. View Cart")
    print("5. Delete Cart")
    print("6. Checkout")
    print("7. Logout")
    ch = int(input("Enter your choice:"))
    return ch


def addProduct():
    pid = int(input("Enter the id of the product:"))
    name = input("Enter the name of the product:")
    price = float(input("Enter its price:"))
    qty = int(input("Enter Stock: "))
    catg = input("Enter Category: ")
    desc = input("Enter Description: ")

    Products[pid] = [name, price, qty, catg, desc]
    print("Product Added Successfully!")


def viewProduct():
    print(Products)


def add_to_cart():
    id = int(input("Enter Product id:"))
    if id in Products.keys():
        cart.append(id)
        print("Cart Updated!")
    else:
        print("Invalid Product id!!")


def viewCart():
    for i in cart:
        if i in Products.keys():
            print(Products[i][0], Products[i][1])


def deleteCart():
    cart.clear()


def checkout():
    tAmount = 0
    j = 1
    for i in cart:
        if i in Products.keys():
            val = Products[i]
            print(j, val[0], val[1])
            price = val[1]
            val[2] -= 1
            tAmount = tAmount + price
            j += 1

    print("=======================")
    print("Bill Amount: ", tAmount)
    cart.clear()


while True:
    choice = printOptions1()
    if choice == 1:
        addProduct()
    elif choice == 2:
        viewProduct()
    elif choice == 3:
        add_to_cart()
    elif choice == 4:
        viewCart()
    elif choice == 5:
        deleteCart()
    elif choice == 6:
        checkout()
    elif choice == 7:
        break
