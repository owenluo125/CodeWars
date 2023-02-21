# https://www.codewars.com/kata/57a77726bb9944d000000b06/python

def mango(quantity, price):
    free = 0
    ogquantity = quantity
    while quantity >= 3:
        quantity -= 3
        free += 1
    return (ogquantity * price) - (free * price)
