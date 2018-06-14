#!/usr/bin/python

def increment(rows):
  for i in range(1,rows+1,2):
    for k in range((rows-i)//2):
      print " ",
    for j in range(0,i):
      print"*",
    print ""
  
def decrement(rows):
  for i in range(rows-2,-1,-2):
    for j in range((rows-i)//2):
      print " ",
    for k in range(0,i):
      print "*",
    print ""

if __name__ == "__main__":
  rows = input("Enter no. of stars:")
  increment(rows)
  decrement(rows)
