# https://www.codewars.com/kata/63ebadc7879f2500315fa07e/python

def cleaned_counts(data):
    newdata = []
    previousdigit = data[0]
    for x in data:
        if x > previousdigit:
            previousdigit = x
        newdata.append(previousdigit)
    return newdata
