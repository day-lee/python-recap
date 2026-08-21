https://www.freecodecamp.org/learn/daily-coding-challenge/08-25
- str.title() 은 첫 글자 대문자, 나머지는 소문자로 바꿈.
- str.capitalize()는 첫 글자만 대문자로 바꾼다.
- re.sub()
- re.split() 
- regex pattern은 string이다. '[_-\s]+'  # _ or - or space, one or more
- enumerate() 는 index와 value를 동시에 접근가능.

# POC
#1 
# chaining replace() method -> not optimal 

def to_camel_case(s):
    clean_s = s.replace('-', " ").replace("_", " ").replace(" ", " ").replace("  ", " ").replace("  ", " ")
    clean_list = clean_s.split(" ")
    r = ""
    for i in range(len(clean_list)):
        if i == 0:
            r += clean_list[i].lower() 
        else: 
            r += clean_list[i].title()  
    print(r)
    return r
to_camel_case("hello world")
to_camel_case("secret agent-X")
to_camel_case("FREE cODE cAMP")


#2 ===========================================================
# re.sub(regex, ' ', s)  # replace by regex pattern -> string

import re

def to_camel_case(s):
    regex = r'[-_\s]+'
    clean_s = re.sub(regex, ' ', s)
    clean_list = clean_s.split(" ")
    r = ""
    for i in range(len(clean_list)):
        if i == 0:
            r += clean_list[i].lower() 
        else: 
            r += clean_list[i].title()  

    print(r)
    return r 

to_camel_case("hello world")
to_camel_case("secret agent-X")
to_camel_case("FREE cODE cAMP")
to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----")



#3 ===========================================================
# re.split(regex, s)  # split by regex pattern -> list 
import re

def to_camel_case(s):
    regex = r'[-_\s]+'
    clean_list = re.split(regex, s)
    r = ""
    for i, word in enumerate(clean_list):
        if i == 0:
            r += word.lower()
        else:
            r += word.title()

    print(r)
    return r 
  
