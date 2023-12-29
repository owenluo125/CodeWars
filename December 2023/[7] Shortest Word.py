# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/python

def find_short(s):
    shortest = len(s.split(" ")[0])
    for x in range(1,len(s.split(" "))):
        if len(s.split(" ")[x]) < shortest:
            print(s.split(" ")[x])
            shortest = len(s.split(" ")[x])
    return shortest
            
