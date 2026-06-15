def ValidProductCode(strParam):
  """
  Have the function ValidProductCode(strParam) take the strParam parameter being passed 
  and determine if the string is a valid industrial product code according to the following rules:

  1. The product code must be between 5 and 15 characters long (inclusive).
  2. It must start with a number.
  3. It can only contain uppercase letters, numbers, and the hyphen (-) character.
  4. It cannot end with a hyphen character.

  If the product code is valid then your program should return the string "true", 
  otherwise return the string "false".

  Examples:
  Input: "9-ABC-123"
  Output: "true"

  Input: "A123-B"
  Output: "false" (Starts with a letter)

  Input: "1-XYZ-"
  Output: "false" (Ends with a hyphen)
  
  Input: "2-AB!"
  Output: "false" (Contains an invalid character '!')
  """

  """ """
  if not (5 <= len(strParam) <= 15):
    return "false"
  if not strParam[0].isdigit():
    return "false"
  if strParam[-1] == "-":
    return "false"
  for char in strParam:
    # 허용되는 안전 조건을 묶은 뒤 그게 아니면 탈락
    # 대문자거나, 숫자거나, - 하이픈이여만 통과. 
    is_valid_char = char.isupper() or char.isdigit() or char == "-"
    if not (is_valid_char):
      return "false"
  return "true"

# Keep this function call here 
print(ValidProductCode("9-ABC-123")) #t
print(ValidProductCode("A123-B")) #F
print(ValidProductCode("1-XYZ-")) #F
print(ValidProductCode("2-AB!"))#F


