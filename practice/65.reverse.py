"""
First Reverse

Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

Examples
Input: "coderbyte"
Output: etybredoc

Input: "I Love Code"
Output: edoC evoL I
"""

def FirstReverse(strParam):
    pass




""" 모범 답안 
  # basic method 
  # result = ""
  # for i in range(len(strParam)):
  #   result += strParam[len(strParam) - i - 1]
  # return result

  # built-in method
  # return "".join(reversed(strParam))

  # Pytonic method
  return strParam[::-1]

"""

print(FirstReverse("I Love Code"))
print(FirstReverse("coderbyte"))