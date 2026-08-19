# https://www.freecodecamp.org/learn/daily-coding-challenge/08-16

# - 파이썬에서 두 리스트의 아이템 종류와 순서가 모두 같다면 두 리스트는 동등(Equal)한 리스트로 평가됨.
# - id()는 객체 메모리 주소를 보여줌. 모든 str의 값이 같게 나오는 이유는 Garbage Collection 과 Re-use 메커니즘 때문임.
# - 파이썬은 더 이상 쓰이지 않는 메모리는 즉시 해제하고 재사용함.
# - 만약 a = sorted(str1), b = sorted(str2) 처럼 변수에 담았다면 메모리가 유지되어서 주소가 달라짐.
# - 메모리 주소가 바뀐 것과는 상관없이 내부 값, 순서 자체가 같으면 True로 평가됨. -> 같은 상황에서 JS는 Reference Type이라 메모리 주소 참조값 비교이므로 False 나옴

#1. use sorted() to compare the string 

def are_anagrams_1(str1, str2):
    print(id(sorted(str1))) #4338399744 
    print(id(sorted(str2))) #4338399744 -> same?! 
    print(id(sorted([1,2,3,4]))) # -> different
    a = sorted(str1)
    b = sorted(str2)
    print('-----variable    -----')
    print(id(a)) # 4338399744
    print(id(b)) # 4338399744 -> different! bc assigned to variable, so memory is maintained.
    print(a == b)
    # Python evaluates the equality of two lists by comparing their elements in order. If both lists have the same elements in the same order, they are considered equal. 
    # list_1 = "".join(sorted(str1.lower().replace(" ", "")))
    # list_2 = "".join(sorted(str2.lower().replace(" ", "")))

    # 파이썬에서는 리스트끼리 비교해도 됨. JS에서는 reference type이라 안됨. 
    list_1 = sorted(str1.lower().replace(" ", ""))
    list_2 = sorted(str2.lower().replace(" ", ""))

    return list_1 == list_2
print(are_anagrams_1("dog", 'cat'))  #f
print(are_anagrams_1("listen", "silent")) #true
print(are_anagrams_1("Hello", "World")) #f
print(are_anagrams_1("A gentleman", "Elegant man")) #true
print('================================')

# ==================================
# hashmap 
# counting .get() 

def are_anagrams_2(str1, str2):
    clean_str1 = clean_counter(str1)
    clean_str2 = clean_counter(str2)

    for char in clean_str1:
        if clean_str1[char] != clean_str2.get(char):
            return False
    return True

def clean_counter(str):
    clean_str = str.lower().replace(" ", "")
    counter = {} 
    for char in clean_str:
        counter[char] = counter.get(char, 0) + 1
    return counter

print(are_anagrams_2("listen", "silent")) # true
print(are_anagrams_2("Hello", "World")) # f
print(are_anagrams_2("A gentleman", "Elegant man")) # true
print(are_anagrams_2("cat", "dog"))  # f