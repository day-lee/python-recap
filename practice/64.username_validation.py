def MediumUsernameValidation(strParam):
  """
  =============================================================================
  [INSTRUCTIONS & CHALLENGE DESCRIPTION]
  =============================================================================
  Have the function MediumUsernameValidation(strParam) take the strParam parameter 
  being passed and determine if the string is a valid username based on 
  the following medium-level rules:

  1. Length Rule: 
     The username must be between 5 and 15 characters long (inclusive).
     
  2. Character Rule: 
     It can only contain lowercase letters, numbers, and the underscore (_) character.
     (Uppercase letters are NOT allowed).
     
  3. Underline Restriction Rule: 
     It must NOT contain two or more underscores in a row. 
     For example, "user__1" is INVALID, but "user_1_a" is VALID.
     
  4. Number Constraint Rule: 
     The username must contain AT LEAST one number. 
     (A username with only letters and underscores is INVALID).

  If the username is valid, your program should return the string "true".
  Otherwise, return the string "false".

  =============================================================================
  [EXAMPLES]
  =============================================================================
  Input: "code_123"
  Output: "true"

  Input: "user__7"
  Output: "false" (Contains consecutive underscores "__")

  Input: "python_coder"
  Output: "false" (Does not contain any numbers)

  Input: "Admin123"
  Output: "false" (Contains an uppercase letter 'A')
  """
  pass








  """ 모범 답안 
  if not (5 <= len(strParam) <= 15):
    return "false"
  
  # 연속하는 언더스코어 __ in operator로 찾기 
  if "__" in strParam:
     return "false"
   
  # 숫자 하나라도 포함여부 플래그로 찾기 
  has_number = False
  for char in strParam: 
      is_valid = char.islower() or char.isdigit() or char == "_"
      if not (is_valid):
         return "false"
      if char.isdigit():
         has_number = True
         
  return "true" if has_number else "false"
"""
# --- Test Cases to Verify Your Logic ---
print(MediumUsernameValidation("code_123"))      # Should print: "true" 
print(MediumUsernameValidation("user__7"))       # Should print: "false" -- double underscore
print(MediumUsernameValidation("python_coder"))   # Should print: "false" - no number
print(MediumUsernameValidation("Admin123"))       # Should print: "false" - upper case
