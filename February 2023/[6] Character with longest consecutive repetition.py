# https://www.codewars.com/kata/586d6cefbcc21eed7a001155/python

def longest_repetition(chars):
    recordLetter = ""
    recordAmount = 0
    currentLetter = ""
    currentAmount = 0
    previousLetter = ""
    for x in range(len(chars)):
        if chars[x] == previousLetter:
            currentAmount += 1
        else:
            currentLetter = chars[x]
            previousLetter = chars[x]
            currentAmount = 1
        if currentAmount > recordAmount:
            recordLetter = currentLetter
            recordAmount = currentAmount
    
    return recordLetter, recordAmount
    
