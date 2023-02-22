# https://www.codewars.com/kata/5547929140907378f9000039/python

def shortcut( s ):
    vowels = ["a","e","i","o","u"]
    newstring = ""
    for x in range(len(s)):
        if s[x] not in vowels:
            newstring += s[x]
    
    return newstring
