#!/usr/bin/python

rows = input("Enter no. of rows:")
for i in range(1,rows+1):
  for j in range(0,i):
    print "*",
  for k in range(((rows-i)*2)-1):
    print " ",
  if i == rows:
    for y in range(rows-1):
      print "*",
  else:
    for x in range(0,i):
      print "*",
  print ""

