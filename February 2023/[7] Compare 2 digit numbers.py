# https://www.codewars.com/kata/63f3c61dd27f3c07cc7978de/python

def compare(a, b):
    compare = 0
    b = str(b)
    a = str(a)
    if a[0] in b:
        b = b.replace(str(a[0]), "", 1)
        compare += 50
    if a[1] in b:
        b = b.replace(str(a[1]), "")
        compare += 50
    return str(compare) + "%"
