'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
def majority_element(nums:list[int])-> int:

    pass
















    # majority = None
    # count = 0 

    # for num in nums: 
    #     if count == 0:
    #         majority = num 
    #     count += (1 if num == majority else -1)

    # return majority

    """ 모범 답안1 : 보이어-무어 투표 알고리즘 Boyer-Moore Voting Algorithm 
    # 딕셔너리를 쓰지 않고 공간 복잡도 O(1)으로 푸는 방법

    candidate = None
    count = 0

    for num in nums:
        # 1. 아군 군대가 떨어지면 현재 만난 사람을 새로운 왕의 후보로 임명한다. 
        if count == 0:
            candidate = num 
        # 2. 현재 후보와 같은 사람이면 군대 +1, 다른 사람이면 적군이니까 -1
        count += (1 if num == candidate else -1)
    return candidate 


    모범 답안2: 정렬 후 과반수 인덱스
    # 과반수 Since the majority el always exists, it will guarantee to occupy the middle index once sorted.
    # 과반수니까 정렬 후 중간 인덱스는 항상 과반수에 해당하는 숫자임. 
    nums.sort() 
    return nums[len(nums) // 2]
    """
    # count = {}
    # for num in nums:
    #     count[num] = count.get(num, 0) + 1 
    # # max key를 dict value로 주려면 dict.get 사용 
    # return max(count, key=count.get)

# def majority_element(nums:list[int])-> int:
#     majority = 0
#     majority_key = 0
#     count = {}
#     for num in nums:
#         count[num] = count.get(num, 0) + 1

#     for k, v in count.items():
#         if v > majority:
#             majority = v 
#             majority_key = k 
#     return majority_key


print(majority_element([3,2,3])) #3
print(majority_element([2,2,1,1,1,2,2])) #2
