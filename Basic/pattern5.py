#!/usr/bin/python
rows = input("Enter no. of stars:")
for i in range(1,rows+1,2):
  for k in range((rows-i)//2):
    print " ",
  for j in range(0,i):
    print"*",
  print ""
    
