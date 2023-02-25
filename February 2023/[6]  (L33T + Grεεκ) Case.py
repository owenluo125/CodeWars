# https://www.codewars.com/kata/556025c8710009fc2d000011/python

def gr33k_l33t(string):
    result = ""
    string = string.upper()
    dict = {
    "A": 'α',
    "B": 'β',
    "C": 'c',
    "D": 'δ',
    "E": 'ε',
    "F": 'f',
    "G": 'g',
    "H": 'h',
    "I": 'ι',
    "J": 'j',
    "K": 'κ',
    "L": 'l',
    "M": 'm',
    "N": 'η',
    "O": 'θ',
    "P": 'ρ',
    "Q": 'q',
    "R": 'π',
    "S": 's',
    "T": 'τ',
    "U": 'μ',
    "V": 'υ',
    "W": 'ω',
    "X": 'χ',
    "Y": 'γ',
    "Z": 'z'}
    
    for x in string:
        if x in dict:
             result += dict[x]
        else:
            result += x
    return result
