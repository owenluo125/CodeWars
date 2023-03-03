# https://www.codewars.com/kata/57a429e253ba3381850000fb/python

def bmi(weight, height):
    bmi = weight / height**2
    return "Underweight" if bmi <= 18.5 else "Normal" if bmi <= 25 else "Overweight" if bmi <= 30 else "Obese"
