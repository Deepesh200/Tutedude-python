'''Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.'''

try:
    file1 = open('sample.txt','r')
    reading_file1 = file1.readline()
    print("Line 1 : ",reading_file1)
    reading_file2 = file1.readline()
    print("Line 2 : ",reading_file2)

    file1.close()
except FileNotFoundError:
    print("The File simple.txt not found.")