# https://www.codewars.com/kata/65127141a5de2b1dcb40927e/python

def spin_around(lst):
    return abs((lst.count("left") - lst.count("right"))) // 4
