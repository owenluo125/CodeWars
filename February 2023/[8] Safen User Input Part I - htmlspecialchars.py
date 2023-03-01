# https://www.codewars.com/kata/56bcaedfcf6b7f2125001118/python

def html_special_chars(data): 
    newdata = ""
    for x in range(len(data)):
        if data[x] == "<":
            newdata += "&lt;"
        elif data[x] == ">":
            newdata += "&gt;"
        elif data[x] == '"':
            newdata += "&quot;"
        elif data[x] == "&":
            newdata += "&amp;"
        else:
            newdata += data[x]
    return newdata
