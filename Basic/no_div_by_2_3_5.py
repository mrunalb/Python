def div(num):
  if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    result = "number is divisible by 2, 3 and 5"
  elif num % 2 == 0 and num % 3 == 0:
    result = "number is divisible by 2 and 3"
  elif num % 3 == 0 and num % 5 == 0:
    result = "number is divisible by 3 and 5"
  elif num % 2 == 0 and num % 5 == 0:
    result = "number is divisible by 2 and 5"
  elif num % 2 == 0:
    result = "number is divisible by 2"
  elif num % 3 == 0:
    result = "number is divisible by 3"
  elif num % 5 == 0:
    result = "number is divisible by 5"
  else:
    result = "number is not divisible by 2 or 3 or 5"
  return result
  
if __name__ == "__main__":
  print("This is to find the numbers divisible by 2, 3, 5: ")
  num = input("Enter a number: ")
  result = div(num)
  print(result)
