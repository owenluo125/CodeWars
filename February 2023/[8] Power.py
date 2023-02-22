# https://www.codewars.com/kata/562926c855ca9fdc4800005b/python

def number_to_pwr(number, p): 
    fin = 1
    for x in range(p):
        fin *= number
    return fin
