# https://www.codewars.com/kata/554b4ac871d6813a03000035/python

def high_and_low(numbers):
    numbersplit = numbers.split(" ")
    highest = int(numbersplit[0])
    lowest = int(numbersplit[0])
    for x in range(len(numbersplit)):
        if int(numbersplit[x]) > highest:
            highest = int(numbersplit[x])
        elif int(numbersplit[x]) < lowest:
            lowest = int(numbersplit[x])
        else:
            pass
    return str(highest) + " " + str(lowest)
