# https://www.codewars.com/kata/5831c204a31721e2ae000294/python

def swap(st):
    final = ""
    for x in range(len(st)):
        if st[x] in "aeiou":
            final += st[x].upper()
        else:
            final += st[x]
    return final
