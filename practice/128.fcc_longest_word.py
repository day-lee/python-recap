"""
https://www.freecodecamp.org/learn/daily-coding-challenge/11-20

- declarative vs imperative programming
- Try to think of built-in functions first! 
- max(list, len=callable)는 길이가 같은 단어가 있다면 가장 먼저 등장한 단어를 반환함 
- re.findall(regex, str)은 패턴 일치하는 부분을 찾아 리스트로 반환함. 일치하는게 없으면 빈 리스트 리턴 
- [a-zA-Z]+는 알파벳 대소문자 1글자 이상 연속된 것 추출 

선언형 도구: list comprehension, 내장 함수들을 먼저 떠올린다. 

절차적 HOW: 특수문자 지우고, 뒤집어서 딕셔너리 넣고, 키만 뽑아서 정렬해서 첫번째 값 가져와야지.
선언적 WHAT: 이 문장에서 알파벳 단어들 골라서 (패턴에 맞는것만 다 가져와 findall()) 그중 길이가 최대인 요소 찾아야지 (max())
"""

import re
def longest_word_optimal(sentence):
    regex = r'[a-zA-Z]+'
    words = re.findall(regex, sentence)
    print(max(words, key=len))
    return max(words, key=len)
longest_word_optimal("Hello coding challenge.") # challenge
longest_word_optimal("A tie? No way!") # tie
longest_word_optimal("Do Try This At Home.") # This
print('===========================================')


def longest_word_1(sentence):
    clean_sentence = sentence.replace(".", '').replace("!","").replace("?","").replace("'","")
    new_list = list(reversed(clean_sentence.split()))
    r = {len(word): word for word in new_list}
    keys = sorted(r, reverse=True)
    idx = keys[0]
    print(r[idx])
    return r[idx]

longest_word_1("Hello coding challenge.") # challenge
longest_word_1("A tie? No way!") # tie
longest_word_1("Do Try This At Home.") # This
print('===========================================')


import re
def longest_word_2(sentence):
    clean_sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)
    sentence_list = clean_sentence.split()
    r = max(sentence_list, key=len)
    print(r)
    return r

longest_word_2("Do Try This At Home.") # This
longest_word_2("A tie? No way!") # "tie".
longest_word_2("Wouldn't you like to know.") # Wouldnt