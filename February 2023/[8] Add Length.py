# https://www.codewars.com/kata/559d2284b5bb6799e9000047/python

def add_length(str_):
    newstr2 = []
    newstr1 = str_.split(" ")
    for x in range(len(newstr1)):
        newstr2.append(newstr1[x] + " " + str(len(newstr1[x])))
    return newstr2
    
