#!/usr/bin/python

print("We are checking whether the string is palindrome or not..!")
str1 = input("Enter a string:")
rev = str1[-1::-1]
if(str1 == rev):
  print("String is palindrome")
else:
  print("String is not palindrome")
  
