"""
https://www.freecodecamp.org/learn/daily-coding-challenge/11-11
- count vowels and consonant
- set(iterable) to avoid duplicate
    set()는 스트링, 리스트 모두 받을 수 있음 
    set()가 좋은 이유는 검색 속도가 더 빨라지기 때문 O(1)
- set() + IN operator  
    set()는 내부적으로 membership 체크가 더 빠르다. 내부적으로 해쉬 테이블 구조를 갖기 때문이다. 
    
- sum() 
    sum(iterable, start)에서 start는 초기 시작 값을 할당할 수 있음  
    sum([1, 1, 1]) 은 3 리턴함 

"""

def count(s):
    lowered_s = s.lower()
    vowels = 'aeiou'
    v = 0
    c = 0
    for char in lowered_s:
        if char.isalpha():
            if char in vowels:
                v += 1
            else: 
                c += 1
    print([v, c])
    return [v, c]

# count("Hello World") # [3, 7]
# count("The quick brown fox jumps over the lazy dog.") # [11, 24]
# count("Hello, World!") # [3, 7].

# 여러 테크닉이 들어갔지만 사실 메모리적으로나 속도적으로나 효율적이지 않음.
def count_2(s):
    vowels = set('aeiou')
    alphabet_s = [ char.lower() for char in s if char.isalpha()]
    alphabet_s_len = len(alphabet_s)
    count_vowels = sum(1 for char in alphabet_s if char in vowels)
    # print([count_vowels, alphabet_s_len - count_vowels])
    return [count_vowels, alphabet_s_len - count_vowels]

count_2("Hello World") # [3, 7]
count_2("The quick brown fox jumps over the lazy dog.") # [11, 24]
count_2("Hello, World!") # [3, 7].


