# https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/python

def to_csv_text(array):
    return(str(array).replace('],', '\n').replace('[', '').replace(']', '').replace(' ', ''))   
