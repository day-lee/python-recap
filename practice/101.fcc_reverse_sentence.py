# https://www.freecodecamp.org/learn/daily-coding-challenge/09-11
"""
- list.reverse(): modify the original list, in-place reversal
- reversed(list) -> new iterator, memory-efficient, reversed copy
- list slicing [::-1] : quick, but high memory consumption 

use-case
1. 리스트를 뒤집어야 할 경우: 타임 스탬프나 거래 내역에서 가장 최근 것부터 나열하고 싶은 경우 
2. sort()된 리스트를 뒤집어야 할 떄, 예: 내림차순으로 정렬된 데이터를 다시 오름차순으로 보여주고 싶을 때 re-sorting 보다 빠르다.
3. LIFO: last in first out 을 처리할 때 

https://www.datacamp.com/tutorial/python-reverse-list
"""

# 비추 
def reverse_sentence(sentence):
    clean = sentence.split()
    r = [ clean[len(clean) - 1 - i] for i, char in enumerate(clean) ]
    return " ".join(r)
reverse_sentence("world hello")



# list.reverse()
def reverse_sentence_2(sentence):
    clean = sentence.split()
    clean.reverse()
    # reversed(clean) # suitable for large dataset
    return " ".join(clean)
reverse_sentence_2("world hello")
reverse_sentence_2("import    default   function  export") # "export function default import".



# reversed(list) - suitable for large dataset
def reverse_sentence_3(sentence):
    clean = sentence.split()
    r = reversed(clean)
    return " ".join(r)
reverse_sentence_3("world hello")



# 4
def reverse_sentence_4(sentence):
    clean = sentence.split() # remove the spaces, turn into a list 
    return " ".join(clean[::-1])
reverse_sentence_4("world hello")
