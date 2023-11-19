https://www.codewars.com/kata/57126304cdbf63c6770012bd/python

def is_digit(s):
    try:
        float(s)
        return True
    except:
        return False
