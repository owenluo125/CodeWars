# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/python

def human_years_cat_years_dog_years(human_years):
    if human_years != 1:
        a = 1
        years = human_years - 2
    else:
        years = 0
        a = 0
        
    return [human_years,15+(a)*9+(years)*4,15+(a)*9+(years)*5]
