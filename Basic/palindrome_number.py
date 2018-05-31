def palindrome(num):
  Rev = 0
  num1 = num
  while num > 0:
    R = num % 10
    Q = num // 10
    num = Q
    Rev = (Rev *10) + R
  if num1 == Rev:
    result = "number is palindrome"
  else:
    result = "number is not a palindrome"
  return result

if __name__ == "__main__":
  num = input("Enter a number:")
  result = palindrome(num)
  print(result)
