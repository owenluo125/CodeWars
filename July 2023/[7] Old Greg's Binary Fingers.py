# https://www.codewars.com/kata/565f1bd8f97d3e59c400014a/python

def binary_fingers(bin_string):
    fingers = []
    combo = {
        0:"Pinkie",
        1:"Ring",
        2:"Middle",
        3:"Index",
        4:"Thumb"
    }
    for x in range(len(bin_string)):
        if int(bin_string[x]) == 1:
            fingers.append(combo[x+5-len(bin_string)])
    
    return fingers
