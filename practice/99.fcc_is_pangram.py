# https://www.freecodecamp.org/learn/daily-coding-challenge/09-03
"""
- set comprehension {}: dedup while looping
- set는 순서 상관없음. element만 일치하면 equality check true나옴 
"""


def is_pangram(sentence, letters):
    dedup_nospace_lower = set("".join(sentence.split()).lower())
    
    new_str = ""
    for char in dedup_nospace_lower:
        if char.isalpha():
            new_str += char

    clean_sentence = "".join(sorted(new_str))
    sorted_letters = "".join(sorted(letters))

    print(clean_sentence, sorted_letters)
    print(clean_sentence == sorted_letters)
    return clean_sentence == sorted_letters
# is_pangram("hello", "helo")
# is_pangram("hello world", "helowrd")
# is_pangram("Hello World!", "helowrd")



def is_pangram_2(sentence, letters):
    # sentence: remove non alphabet, remove space, remove dup, lower 
    # set comparison -> element, order doesn't matter
    # - set 성질 이용하기 dedup, 순서 상관없음 
    # - isalpha 먼저 필터링

    clean_s = [char.lower() for char in sentence if char.isalpha()]
    
    dedup_sentence = set(clean_s)
    set_letters = set(letters)

    print(dedup_sentence == set_letters)
    return dedup_sentence == set_letters

is_pangram_2("hello", "helo") # True
is_pangram_2("hello world", "helowrd") # True
is_pangram_2("Hello World!", "helowrd")  # True
is_pangram_2("freeCodeCamp", "frcdmp") #False



def is_pangram_3(sentence, letters):
    # dedup first: less computation 
    # set comprehension

    sentence_set = {char.lower() for char in sentence if char.isalpha()}
    letters_set = set(letters)

    print(sentence_set == letters_set)
    return sentence_set == letters_set

print("=====================================")
is_pangram_3("hello", "helo") # True
is_pangram_3("hello world", "helowrd") # True
is_pangram_3("Hello World!", "helowrd")  # True
is_pangram_3("freeCodeCamp", "frcdmp") #False