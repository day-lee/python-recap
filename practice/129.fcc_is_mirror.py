"""
https://www.freecodecamp.org/learn/daily-coding-challenge/09-29

- re.findall(regex, str): 패턴은 패턴에 맞는 것만 찾아서 리턴해줌 
- re.sub(regex, replace, str): 은 패턴에 맞는 것만 찾아서 replace 변환해줌  
"""

import re

def is_mirror(str1, str2):
    clean_str_1 = clean_str(str1)
    clean_str_2 =clean_str(str2)
    print(clean_str_1 == clean_str_2[::-1])
    return clean_str_1 == clean_str_2[::-1]

def clean_str(word):
    regex = r'[a-zA-Z]+'
    r = re.findall(regex, word)
    return "".join(r)

is_mirror("helloworld!", "helloworld") #False
is_mirror("Hello World", "!dlroW !olleH") #true
is_mirror("RaceCar", "RaceCar") #False

