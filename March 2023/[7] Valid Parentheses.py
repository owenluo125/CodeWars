# https://www.codewars.com/kata/6411b91a5e71b915d237332d/python

def valid_parentheses(paren_str):
    while "()" in paren_str:
        paren_str = paren_str.replace("()","")
    
    return True if paren_str == "" else False
