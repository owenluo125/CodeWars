# https://www.codewars.com/kata/563e320cee5dddcf77000158/python

def get_average(marks):
    average = 0
    for x in marks:
        average += x
    return int(average / len(marks))
