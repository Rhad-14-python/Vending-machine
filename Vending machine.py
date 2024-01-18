# Assessment 2: Vending Machine 
all_the_products = [
    {
        "product_No.": 0,
        "product_Name": "Mang Juan",
        "price": 3
    },
    {
        "product_No.": 1,
        "product_Name": "Snacku",
        "price": 6,
    },
    {
        "product_No.": 2,
        "product_Name": "Doowee Donut",
        "price": 2,
    },
    {
        "product_No.": 3,
        "product_Name": "Cheese Ball",
        "price": 8,
    },
    {
        "product_No.": 4,
        "product_Name": "Yipyap",
        "price": 10
    },
    {
        "product_No.": 5,
        "product_Name": "Roi's Fish Cracker",
        "price": 4,
    },
    {
        "product_No.": 6,
        "product_Name": "Red Chili",
        "price": 3,
    },
    {
        "product_No.": 7,
        "product_Name": "Pik-Nik",
        "price": 20,
    },
    {
        "product_No.": 8,
        "product_Name": "Cheesy Puffs",
        "price": 25,
    },
    {
        "product_No.": 9,
        "product_Name": "Tiwi Mosy-Mosy Fruit Sip",
        "price": 6,
    },
    {
        "product_No.": 10,
        "product_Name": "Mello Choco Marshmallow Bar",
        "price": 15,
    },
    {
        "product_No.": 11,
        "product_Name": "C2",
        "price": 4,
    },
    {
        "product_No.": 12,
        "product_Name": "Mogu Mogu",
        "price": 2,
    },
    {
        "product_No.": 13,
        "product_Name": "Zesto Big 250",
        "price": 2
    },
    {
        "product_No.": 14,
        "product_Name": "Milo",
        "price": 3
    },
    {
        "product_No.": 15,
        "product_Name": "Sarsi",
        "price" : 3,
    },
]
product=[]
reciept="""
\t\tPRODUCT -- PRICE
"""
sum= 0
run=True

print("-------Filipino products in a Venging Machine-------")
print("----------All the Pinoy foods inside----------")

for i in all_the_products:
    print(f"Products: {i['product_Name']} --- Prices --- {i['price']} --- Products number --- {i['product_No.']}")
def VendingMachine(products_in_stock, run, the_product):
    while run:
        buy_product= int(input("\n\n Enter the product number you want to purchase"))
        
        if buy_product < len(products_in_stock):
            product.append(products_in_stock[buy_product])
        else: 
            print("I'm sorry the product number is wrong")
        more_products= str(input("Press any key to add more foods or drinks and press x to exit."))
        if more_products=="x":
            run = False
    order=int(input(" 1. print the receipt?? 2. only the print total sum.."))
    if order == 1:
        print(reciept,the_product, reciept)
    elif order == 2:
        print(sum(the_product))
    else:
        print("Wrong entry")

def sum (the_product): 
    sum = 0
    for i in the_product:
        sum+=i["price"]
    return sum

def create_reciept(product_Name): 
    for i in product_Name:
        reciept += f"""\t{i["product_Name"]} -- {i['price']}"""
    reciept += f"""\tTotal---{sum(product)}"""
    return reciept
VendingMachine(all_the_products, run, product)