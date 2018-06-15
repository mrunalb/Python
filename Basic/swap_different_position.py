#!/usr/bin/python

num1 = input("Enter no.1:")
num2 = input("Enter no.2:")
position1 = input("Enter position for no.1:")
position2 = input("Enter position for no.2:")
numofbits = input("Enter no.of bits:")
no = (1 << numofbits)-1
mask1 = (no << (position1 - numofbits))
mask2 = (no << (position2 - numofbits))
x_part = num1 & mask1
y_part = num2 & mask2
new_mask1 = ~ mask1
new_mask2 = ~ mask2
if (position1 > position2):
  y_part = y_part << (position1-position2)
  x_part = x_part >> (position1-position2)
else:
  y_part = y_part >> (position2-position1)
  x_part = x_part << (position2-position1)
new_num1 = num1 & new_mask1
new_num2 = num2 & new_mask2
swapped_num1 = new_num1 | y_part
swapped_num2 = new_num2 | x_part
print("num1 after swapping:",swapped_num1)
print("num2 after swapping:",swapped_num2)
