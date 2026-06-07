"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

1. two pointer
2. slicing [::]

"""
#floor division



# # 1. two pointer 
# # 1. clean the data: lower(), replace(), isalnum() w/ for loop, list comprehension, join()

# # 2. first, end is same, loop through each index, range(len())/ 2, if condition False return early, enumerate.. 

# def isPalindrome(s:str) -> bool:
#     cleaned_str = "".join([char.lower() for char in s if char.isalnum()])
#     for i in range(round(len(cleaned_str)/2)):
#         end = len(cleaned_str) - 1 - i
#         if cleaned_str[i] != cleaned_str[end]:
#             return False
#     return True 
        
# # 2.slice 

# def isPalindrome(s:str) -> bool:
#     cleaned_str = "".join([char.lower() for char in s if char.isalnum()])
#     return cleaned_str == cleaned_str[::-1]


# # two pointer 
# def isPalindrome(s:str) -> bool:
#     # 1. clean the str: lower(), isalnum() & for loop , turn it into str with join()
#     cleaned_s = "".join(char.lower() for char in s if char.isalnum())
#     # print(cleaned_s)
#     # 2. checking palindrome: for loop with index range(), len(), checking start and end, round() round half to even 

#     # iterating by index 
#     last_index = len(cleaned_s) -1
#     # 절반만 비교 // 연산자로 내림 변환 
#     for i in range(len(cleaned_s) // 2):
#         if cleaned_s[i] != cleaned_s[last_index - i]:
#             return False 
#     return True

# slice() 메소드 활용
def isPalindrome(s:str) -> bool:
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1] # pythonic string reversal 

   #슬라이싱은 [시작:끝:증감] 구조. 시작 끝을 비우면 전체 대상. 1은 앞에서부터 1칸씩 더하면서 움직임. -1은 뒤에서부터 1칸씩 움직(반대로) 
   # [::1]은 C언어 레벨에 최적화됨 속도가 빠르다.

print(isPalindrome("A man, a plan, a canal: Panama")) #T
print(isPalindrome("race a car")) #F
print(isPalindrome(" "))#T
print(isPalindrome("1221")) #T


# ==============================================================

# def isPalindrome(s: str) -> bool:
#     # print(s.replace(" ", "").lower())
#     clean_str =  "".join([char for char in s if char.isalnum() ]).lower()
#     print(clean_str)
#     for i in range(round(len(clean_str) / 2)):
#         print(f"start {clean_str[i]}")
#         print(f"end: {clean_str[len(clean_str) - 1 -i]}")
        
#         if clean_str[i] == clean_str[len(clean_str) - 1 -i]:
#             continue
#         else: 
#             return False
#     return True

# print(isPalindrome("A man, a plan, a canal: Panama"))
