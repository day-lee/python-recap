""" leetcode 1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""
def twosum(nums:list[int], target:int) -> list[int]:
    pass









print(twosum(nums = [2,7,11,15], target = 9))  # [0, 1]
print(twosum(nums = [3,2,4], target = 6)) # [1, 2]
print(twosum(nums = [3,3], target = 6)) #[0, 1]
print(twosum(nums = [0], target = 6)) #[]

""" 모범 답안 
# 만약 해시맵에 있으면 리턴하고, 없으면 만든다. 
def twosum(nums:list[int], target:int) -> list[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i 
    return []
"""

# 해시맵을 만드는건 맞는데, 중복 숫자면 작동을 안하게 됨..
# def twosum(nums:list[int], target:int) -> list[int]:
#     if len(nums) < 2:
#         return []
#     hashmap = {num: i for i, num in enumerate(nums)}

#     for i in range(len(nums)):
#         complement = target - nums[i] 
#         if complement in hashmap and hashmap[complement] != i:
#             return [i,  hashmap[complement]]
#     return []
















""" 모범 답안
값: 인덱스 해시맵을 만들고,
인덱스를 사용하는 반복문을 돌면서 
임시 보수를 먼저 계산해두고,
만약 해시맵에 임시 보수가 존재하고, 그 인덱스가 현재의 인덱스가 아니면, 두 인덱스를 리턴함 
"""