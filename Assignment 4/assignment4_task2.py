'''Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.'''

write = input ("Enter text to write to the file: " )

file1 = open ("output.txt", "w")
writting_file = file1.write(write + '\n')
file1.close()

print ("Data successfully written to output.txt")

apend = input ("Enter additional text to appent: ")
file2 = open ("output.txt", "a")
append_file = file2.write(apend + '\n')
file2.close()
print ("Data successfully appended.")

file3 = open ("output.txt", "r")
reading_file = file3.read()
print (reading_file)
file3.close()