def cls(Maths,Science,English,Marathi,Sanskrit,Hindi):
  Total = Maths+Science+English+Marathi+Sanskrit+Hindi
  percent = (Total / 6)
  if Maths >= 35 and Science >= 35 and English >= 35 and Marathi >= 35 and Sanskrit >= 35 and Hindi >= 35:
    if percent >= 75:
      result = "First class with distinction!"
    elif percent < 75 and percent >= 60:
      result = "First class!"
    elif percent < 60 and percent >= 50:
      result = "Second class!"
    elif percent < 50 and percent >= 35:
      result = "Pass class"
  else:
    result = "FAIL! Please study well!"      
  return result

if __name__ == "__main__":
  print("This is to find the class of the student:")
  Maths = input("Enter maths score:")
  Science = input("Enter Science score:")
  English = input("Enter English score:")
  Marathi = input("Enter Marathi score:")
  Sanskrit = input("Enter Sanskrit score:")
  Hindi = input("Enter Hindi score:")
  result = cls(Maths,Science,English,Marathi,Sanskrit,Hindi)
  print(result)
