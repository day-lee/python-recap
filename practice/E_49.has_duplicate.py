'''
Given an integer array nums, 
return true if any value appears more than once in the array,
otherwise return false.

[1,2,3,1] True 
'''

def has_duplicate(nums: list[int]) -> bool:

    pass











    # count = {}
    # for num in nums:
    #     if num in count:
    #         return True 
    #     count[num] = 1
    # return False

    # return len(nums) != len(set(nums))

    # count = {} 
    # for num in nums:
    #     if num in count:
    #         return True
    #     count[num] = 1
    # return False    
    
    # 오버 엔지니어링 
    # count = {} 
    # for num in nums:
    #     count[num] = count.get(num, 0) + 1 
    #     if count[num] >= 2:
    #         return True
    # return False     

    """ 모범 답안
    # 1. compare the length with set() 
    # return len(set(nums)) != len(nums)

    # 2. hashmap with early return 
    count = {}
    for num in nums:
        if num in nums:
            return True # exists!
        count[num] = 1 
    return False 
    """
print(has_duplicate([1, 2, 3, 4, 5, 5])) # True
print(has_duplicate([1, 2, 3])) # F

