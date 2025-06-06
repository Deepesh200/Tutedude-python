'''Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''

from math import *
num = float(input("Enter a number :- "))
if num > 0:
    squareroot = sqrt(num)
    logarithm = log(num)
else:
   print ("Wrong input Please enter a correct input")

sine_result = sin(num) 

print("Square root :- ",squareroot)
print("logarithm :- ",logarithm)
print("Sine :- ", sine_result)
