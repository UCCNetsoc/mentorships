import json

customers = [] # both customers and products are equal to an empty array
products = []

def split_by_comma(line) -> list:      # return type can be defined with an arrow
    """
        returns the given str as a list split on commas
        
        @type line: str
        @rtype: list(str)
    """
    line = line.split(",")  # split the string on commas into a list
    # line.remove("\n")       # remove the '\n' (newline character)
    return line             # return the list

with open('customers.txt', "r") as customers_file:
    for line in customers_file:                   # for each line in the file do the following 
        line = line.replace("\n", "")
        customers.append(split_by_comma(line))      # insert the returned list into the customers list
                                                    # customers is a list of lists

with open('products.txt', "r") as products_file:
    for line in products_file:                      # ...
        line = line.replace("\n", "")
        products.append(split_by_comma(line))      # insert the returned list into the customers list
                                                     # products is a list of lists


def user_product_pair():
    dict = {}
    for customer in customers:
        for product in products:
            if customer[2] == product[0]:
                dict[customer[1]] = product[1]
    return dict

def customers_to_dict(customers: list):
    with open('customers_dict.json', 'w') as customers_json:
        for customer in customers:
            obj = {}
            obj['id'] = customer[0]
            obj['name'] = customer[1]
            obj['ordered'] = customer[2]
            customers_json.write(f"{obj}\n")

def products_to_json(products: list):
    with open('products.json', 'w') as products_json:
        l = []
        for product in products:
            obj = {}
            obj['id'] = product[0]
            obj['name'] = product[1]
            obj['seller'] = product[2]
            l.append(obj)
        products_json.write(json.dumps(l))

def read_to_dict():
    with open('customers_dict.txt', "r") as customers_dict:
        json = eval(customers_dict.read())
        print(json)

products_to_json(customers)