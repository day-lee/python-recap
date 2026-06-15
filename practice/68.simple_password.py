
def simple_password(password_str: str) -> bool:
    """Check if the given string meets all password strength requirements.

    The password must satisfy the following 5 strict conditions:
    1. Must contain at least one uppercase letter.
    2. Must contain at least one number.
    3. Must contain at least one punctuation mark (. , ! ? : ;).

    4. Cannot contain the word "password" (case-insensitive).
    5. Length must be between 8 and 30 characters (inclusive).

    Args:
        password_str (str): The password string to validate.

    Returns:
        bool: True if all requirements are met, False otherwise.
    """


    """ 모범 답안: set(), early return 
    if not ( 8 <= len(password_str) <= 30):
        return False
    if "password" in password_str.lower():
        return False 
    
    # set() is quicker
    punctuation_mark = {".", ",", "!", "?", ":", ";"}
    has_number = False 
    has_upper = False 
    has_punctuation_mark = False 

    for char in password_str:
        # 모든 글자를 돌기전에 혹시 세 조건을 미리 만족했는지 확인함 
        if has_upper and has_number and has_punctuation_mark:
            break 

        if char.isupper():
            has_upper = True 
        if char.isdigit():
            has_number = True 
        if char in punctuation_mark:
            has_punctuation_mark = True 

    if has_upper and has_number and has_punctuation_mark:
        return True 
    return False 
    """

# Run test cases
if __name__ == "__main__":
    test_cases = [
        ("apple! M7", True),
        ("passWord123!!!!", False),
        ("turkey90AAA!", True),
        ("short1!", False), 
    ]
    
    for pwd, expected in test_cases:
        result = simple_password(pwd)
        print(f"Input: {pwd} -> {result} (Expected: {expected})")
