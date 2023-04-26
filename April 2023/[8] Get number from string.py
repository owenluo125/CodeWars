# https://www.codewars.com/kata/57a37f3cbb99449513000cd8/python

def get_number_from_string(string):
    new = ""
    for x in range(len(string)):
        if string[x].isdigit():
            new += str(string[x])
    return int(new)
