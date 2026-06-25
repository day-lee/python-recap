"""
Codeland Username Validation
Have the function codeland_username_validation(str) take the str parameter being passed and determine 
if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.

Examples
Input: "aa_"
Output: false

Input: "u__hello_world123"
Output: true

"""
def codeland_username_validation(strParam):
    pass














    # if not (4 <= len(strParam) <= 25):
    #     return "false"
    # if not strParam[0].isalpha():
    #     return "false"
    # if strParam[-1].endswith("_"):
    #     return "false" 
    # for char in strParam:
    #     is_allowed = char.isalnum() or "_"
    #     if not is_allowed:
    #         return "false"
    # return "true"

    # if not 4 <= len(strParam)<= 25:
    #     return "false"
    # if not strParam[0].isalpha():
    #     return "false"
    # if strParam[-1] == "_":
    #     return "false"

    # for char in strParam:
    #     if not (char.isalnum() or char == "_"):
    #         return "false"
    # return "true"

    """ 모범 답안
    def codeland_username_validation(strParam):

    if not (4 <= len(strParam) <= 25):
        return "false"
    if not strParam[0].isalpha():
        return "false"    
    if strParam[-1] == "_":
        return "false"

    for char in strParam:
        is_valid = char.isalnum() or char == "_"
        if not (is_valid):
            return "false"
        
    return "true"
    """
print(codeland_username_validation("u__hello_world123")) #T
print(codeland_username_validation("aa_")) #F - len 3
print(codeland_username_validation("_aaasdbe23")) #F starts with _
print(codeland_username_validation("1aaa")) #F starts with number
print(codeland_username_validation("aaa_")) #F ends with _
print(codeland_username_validation("u12345678910111213111113331111")) #F over 25
