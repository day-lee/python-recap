"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""
def isAnagram(s:str, t:str) -> bool: 
    pass 














# 1. sorted 
# 2. Counter: module 
# 3. hashmap: counting up s, counting down t


# def isAnagram(s, t):
#     # 1
#     # early return 
#     if len(s) != len(t):
#         return "false"
#     str_s = sorted(s)
#     str_t = sorted(t)
#     if str_s == str_t:
#         return "true"
#     return "false"

#     # 2
#     from collections import Counter

#     s_counter = Counter(s)
#     t_counter = Counter(t)
#     for char in s_counter:
#         if t_counter[char] != s_counter[char]:
#             return "false"
#     return "true"
#     Counter 객체는 내부적으로 해시맵 사용해서 직접 비교 가능 
#     s_counter == t_counter 

#     #3
#     if len(s) != len(t):
#         return "false"
#     counter = {}
#     for char in s:
#         counter[char] = counter.get(char, 0) + 1 
    
#     for char in t:
#         글자가 없거나 개수가 소진되면 
#         if char not in counter or counter[char] == 0:
#             return "false"
#         counter[char] -= 1 
#     return "true"


# =========================================================
"""
1. sorted 
def isAnagram(s, t):
    if len(s) != len(t):
        return "false" 
    return sorted(s) == sorted(t)

2. Counter: module 
Counter()는 글자수를 O(N)으로 세준다. 
from collections import Counter
def isAnagram(s, t):
    return Counter(s) == Counter(t)

# 3. hashmap: counting up s, counting down t
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    # s count 올리기
    s_count = {} 
    for char in s:
        s_count[char] = s_count.get(char, 0) + 1 

    # s count 내리기: 아예 존재하지 않거나, 개수가 다르게 존재하거나 
    for char in t:
        if char not in s_count or s_count.get(char) == 0:
            return False 
        s_count[char] -= 1

    return True


"""


# early return if lenth doesn't match
# hashmap for counting existing char

# # count() 쓰지 않는게 좋음. 성능 문제 O(n2) 
# def isAnagram(s:str, t:str) -> bool:
#     if len(s) != len(t):
#         return False
#     s_count = {char: s.count(char) for char in s}
#     t_count = {char: t.count(char) for char in t}

#     for char, count in s_count.items():
#         if t_count.get(char) != count:
#             return False 
#     return True

print(isAnagram("rat", "ratt")) # F
print(isAnagram("rat", "raa")) # F
print(isAnagram("anagram", "nagaram")) # T
print(isAnagram("rat", "car")) # F


