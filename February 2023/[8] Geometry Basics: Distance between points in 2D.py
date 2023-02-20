# https://www.codewars.com/kata/58dced7b702b805b200000be/python

def distance_between_points(a, b):
    x = a.x - b.x
    y = a.y - b.y
    return (x**2 + y**2)**.5
