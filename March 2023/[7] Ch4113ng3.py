# https://www.codewars.com/kata/59e9f404fc3c49ab24000112/python

def nerdify(txt):
    dict = {"a":"4",
           "e": "3",
           "l": "1"}
    for x in range(len(txt)):
        if txt[x].lower() in dict and txt[x] != "L":
            txt = txt[:x] + dict[txt[x].lower()] + txt[x+1:]
    return txt
