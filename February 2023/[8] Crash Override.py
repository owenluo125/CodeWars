# https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f/python

def alias_gen(f_name, l_name):
    if ord(f_name[0]) < 59 or ord(l_name[0]) < 59:
        return 'Your name must start with a letter from A - Z.'
    
    return FIRST_NAME[f_name[0].upper()] + " " + SURNAME[l_name[0].upper()]
