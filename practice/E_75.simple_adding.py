def simple_adding(num: int) -> int:
    """
    Coderbyte: Simple Adding

    Return the sum of all numbers from 1 up to the given integer 'num'.
    For example, if the input is 4, it should calculate 1 + 2 + 3 + 4 and return 10.

    [Requirements]
    1. The input 'num' will always be a positive integer (1 <= num <= 1000).
    2. Return the cumulative sum accurately as an integer type.

    Args:
        num (int): The last target positive integer to add up to.

    Returns:
        int: The cumulative sum from 1 to num.

    Examples:
        >>> simple_adding(4)
        10
        >>> simple_adding(12)
        78
        >>> simple_adding(1)
        1
    """
    pass 










    """ 모범답안: 2번 추천 
    # 1. traditional way
    total = 0
    for i in range(1, num+1):
        total += i
    print(total)

    # 2. built-in functions
    return sum(range(1, num + 1))
    
    # 3. recursion 
    if num == 1:
        return 1 
    return num + simple_adding(num-1)
    """
# Test Cases (Uncomment to verify your implementation)
print(simple_adding(4))   # Expected: 10
print(simple_adding(12))  # Expected: 78
print(simple_adding(1))   # Expected: 1
