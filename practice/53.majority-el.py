'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''

def majority_element(nums:list[int])-> int:
    majority = 0
    majority_key = 0
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    for k, v in count.items():
        if v > majority:
            majority = v 
            majority_key = k 
    return majority_key



print(majority_element([3,2,3])) #3
print(majority_element([2,2,1,1,1,2,2])) #2
