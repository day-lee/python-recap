# https://www.freecodecamp.org/learn/daily-coding-challenge/11-03
"""
collections is a built-in library
Counter class: returns dictionary type
total() method is available from Python 3.10 above 

split() takes care of new lines \n, tab \t, spaces 
"""
from collections import Counter

def count_words_1(sentence):
    word_list = sentence.split()
    print(len(word_list))
    return len(word_list)

count_words_1("The missing semi-colon crashed the entire internet.") #7



def count_words_2(sentence):
    word_list = sentence.split()
    c = Counter(word_list)
    print(f'length: {len(c)}')
    print(c.total())
    return c.total()

count_words_2("The missing semi-colon crashed the entire internet.") #7

