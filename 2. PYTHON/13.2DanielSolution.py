menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    subtotal=0
    for codigo, datos in order.items():        
        subtotal += datos["price"]        
    return round (float(subtotal),2)  
    raise NotImplementedError()

print (calculate_subtotal(menu))


def calculate_tax(subtotal):
    tax=0
    for codigo, datos in subtotal.items():        
        tax += datos["price"]*0.15        
    return round (float(tax),2)  
    raise NotImplementedError()
print (calculate_tax(menu))

def calculate_tax(subtotal):
    subtotal= calculate_subtotal(menu)
    tax= subtotal*0.15
    return round (float(tax),2) 
    raise NotImplementedError()
print (calculate_tax(menu))



def summarize_order(order):

   
    subtotal= calculate_subtotal(order)
    tax= calculate_tax(subtotal)
    total = round((subtotal+tax),2)
    n=0 

    for cod, names in order.items():
        n += names["name"]
    return n, total
    
print(summarize_order(menu))