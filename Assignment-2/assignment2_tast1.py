'''Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.'''

number = int(input('Enter a number :- '))

if number % 2 == 0 :
    print(number, "is a even number")
else:
    print(number, "is an odd number")
