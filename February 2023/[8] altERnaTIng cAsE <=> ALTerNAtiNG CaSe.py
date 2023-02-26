# https://www.codewars.com/kata/56efc695740d30f963000557/python

def to_alternating_case(string):
    newstring = ""
    for x in range(len(string)):
        if string[x].isalpha():
            if string[x].isupper():
                newstring += string[x].lower()
            else:
                newstring += string[x].upper()
        else:
            newstring += string[x]
    return newstring
