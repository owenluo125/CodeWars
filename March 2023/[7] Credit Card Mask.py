# https://www.codewars.com/kata/5412509bd436bd33920011bc/python

return masked string
def maskify(cc):
    new = ""
    if len(cc) > 4:
        for x in range(len(cc)-4):
            new += "#"
        new += cc[-4:]
        return new
    return cc
        
