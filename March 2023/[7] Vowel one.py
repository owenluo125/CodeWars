# https://www.codewars.com/kata/580751a40b5a777a200000a1/python

def vowel_one(s):
    vowels = "aeiou"
    new = ""
    for x in range(len(s)):
        if s[x].lower() in vowels:
            new += "1"
        else:
            new += "0"
    return new
