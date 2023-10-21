# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/python

def is_uppercase(inp):
    count = 0
    for x in range(len(inp)):
        if inp[x].islower():
            count += 1
    return True if count == 0 else False
