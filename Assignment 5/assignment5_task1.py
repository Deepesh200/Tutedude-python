'''Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.'''

my_dic = {'Alice': 90, 'Bob': 85, 'Charlie': 95, 'Deepesh': 99} 

name = input("Enter the student's name: ")
if name in my_dic:
    print(name + "'s marks : ",(my_dic[name]))
else:
    print("Student not found.")