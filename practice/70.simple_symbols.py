def simple_symbols(str_param: str) -> bool:
    """
    Coderbyte: Simple Symbols

    Check if all alphabetic characters in the string are surrounded by '+' symbols.

    [Requirements]
    1. If there are no alphabetic characters in the string, return True.
    2. Each letter must be immediately preceded and followed by a '+' symbol.
    3. If the first or the last character of the string is a letter, 
       it cannot be properly surrounded, so return False.

    Args:
        str_param (str): The input string containing letters, numbers, and symbols.

    Returns:
        bool: True if every letter is surrounded by '+' symbols, False otherwise.

    Examples:
        >>> simple_symbols("+d+=3=+s+")
        True
        >>> simple_symbols("f++d+")
        False
        >>> simple_symbols("+a+")
        True
    """
    pass
















    """ 모범 답안 
    # 1. early return for edge case
    # 2. test char in a loop 

    # str_param[0]에서 index error 방지
    if not str_param:
        return True

    # 둘중 하나라도 알파벳 true 면, 결과는 F
    if str_param[0].isalpha() or str_param[-1].isalpha():
        return False
    
    for i, char in enumerate(str_param):
        if char.isalpha():
            # 둘 중하나라도 + 가 아니면 F 
            if str_param[i-1] != "+" or str_param[i+1] != "+":
                return False 
    return True
    """
    
print(simple_symbols("f++d+")) #false
print(simple_symbols("+d+=3=+s+")) #true
print(simple_symbols("+a+")) #true
print(simple_symbols("+3+")) #true
print(simple_symbols("+")) #true
print(simple_symbols(" ")) #true
print(simple_symbols("")) #true


    


