# https://www.codewars.com/kata/56f3f6a82010832b02000f38/python

def describe_age(a):
    return"You're a(n) "+("kid"if a<13else"teenager"if a<18else"adult"if a<65else"elderly")
