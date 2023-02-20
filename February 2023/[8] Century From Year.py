# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/python

def century(year):
    total = 0
    while True:
        if year - total*100 <= 0:
            break
        else:
            total += 1
    return total
