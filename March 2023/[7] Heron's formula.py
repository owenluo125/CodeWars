# https://www.codewars.com/kata/57aa218e72292d98d500240f/python

def heron(a, b, c):
    s = (a+b+c)/2
    return round((s * (s-a) * (s-b) * (s-c))**.5, 2)
