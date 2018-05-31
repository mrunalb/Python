def cnt(statement): 
  l = len(statement)
  if l < 20:
    print(l)
    result = "line is too short"
  elif l >=20 and l < 80:
    print(l)
    result = "line is sufficient in length"
  else:
    print(l)
    result = "line is too long"
  return result

if __name__ == "__main__":
  print("This is to find length of the line: ")
  statement = raw_input("Enter a line:")
  result = cnt(statement)
  print(result)
