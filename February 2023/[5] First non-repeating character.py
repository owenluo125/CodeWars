# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/python

def first_non_repeating_letter(string):
    for x in range(len(string)):
        if string[x].isalpha():
            if string.count(string[x].lower()) + string.count(string[x].upper()) == 1:
                return string[x]
        else:
            if string.count(string[x]) == 1:
                return string[x]
    return ""
