#!/usr/bin/python

num1 = input("Enter no.1:")
num2 = input("Enter no.2:")
position = input("Enter position:")
numofbits = input("Enter no.of bits:")
no = (1 << numofbits)-1
mask = (no << (position - numofbits))
x_part = num1 & mask
y_part = num2 & mask
new_mask = ~ mask
new_num1 = num1 & new_mask
new_num2 = num2 & new_mask
swapped_num1 = new_num1 | y_part
swapped_num2 = new_num2 | x_part
print("num1 after swapping:",swapped_num1)
print("num2 after swapping:",swapped_num2)
