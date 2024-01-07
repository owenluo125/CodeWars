https://www.codewars.com/kata/57d06663eca260fe630001cc/python

import math

def olympic_ring(string):
    medals = 0
    dict = {
        "O" : 1,
        "o" : 1,
        "b" : 1,
        "d" : 1,
        "D" : 1,
        "q" : 1,
        "R" : 1,
        "Q" : 1,
        "p" : 1,
        "P" : 1,
        "e" : 1,
        "a" : 1,
        "A" : 1,
        "g" : 1,
        "B" : 2
    }
    for x in string:
        if x in dict:
            medals += dict.get(x)
    if math.floor(medals/2) == 2:
        return "Bronze!"
    elif math.floor(medals/2) == 3:
        return "Silver!"
    elif math.floor(medals/2) > 3:
        return "Gold!"
    else:
        return "Not even a medal!"
