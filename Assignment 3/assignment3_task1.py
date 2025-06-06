'''Task 1: Calculate Factorial Using a Function


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.'''

def facto(n):
    result = 1 
    for i in range(1, n + 1):
        result *= i  
    return result  
n1 = int(input("Enter a Number :- "))
factorialis = facto(n1)
print("Factorial of", n1, "is", factorialis)
