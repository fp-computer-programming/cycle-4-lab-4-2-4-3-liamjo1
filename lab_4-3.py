"""
Create a Python file named lab_4-2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_4-2.py
Create a variable called school and set it equal to "Fairfield Prep".
Write a statement that splits "Fairfield" and stores it as first_half, and a similar statement that splits " Prep" and stores it as second_half.
Print each half on its own line, then print the two halves joined together using concatenation.

____________________________________

Create a Python file named lab_4-3.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a program that contains a conditional similar to that on slide 4 that will compare two strings 
provided by the user and return if the strings are equal, one string is greater than the other, or one string is less than the other.


"""
# Liam O'Hara

school = "Fairfield Prep"
# create school variable - O'Hara

first_half = school[0:9]
# slice variable and store first half in its own variable - O'Hara

second_half = school[10:14]
# slice variable and store second half in its own variable - O'Hara

print(first_half)
print(second_half)
# printing both halves on their own line - O'Hara

print(first_half + " " + second_half)
# concatenate both and print with correct spacing - O'Hara

s1 = input("Enter string one:")
s2 - input("Enter ")