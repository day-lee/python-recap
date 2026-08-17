- sorted(str/iterable)은 list 형식을 리턴한다. 
- 3글자 이하는 바뀔게 없으므로 조건 변경

def jbelmu(text):
    result = []
    text_list = text.split()
    for word in text_list:
        if len(word) > 3:
            middle_text = word[1: -1]
            sorted_text = "".join(sorted(middle_text)) 
            new_word = word[0] + sorted_text + word[-1]
            result.append(new_word)
        else: 
            result.append(word)
    print(" ".join(result))
    return " ".join(result)

# 1. make a list of words: split()
# 2. access in a loop, if len is > 2, slice 1:-1
# 3. sliced word sorted() 
# 4. reassemble 1, sorted ,-1
# 5. add to a new list, turn back into string 

jbelmu("hello world") 
# "hello wlord"
jbelmu("freecodecamp is my favorite place to learn to code")
#"faccdeeemorp is my faiortve pacle to laern to cdoe"
jbelmu("the quick brown fox jumps over the lazy dog")
# "the qciuk borwn fox jmpus oevr the lazy dog".






# ==== first try ====
# def jbelmu(text):
#     result = []
#     text_list = text.split()
#     for word in text_list:
#         char_list = list(word)
#         if len(char_list) > 2:
#             middle_text = char_list[1: -1]
#             # print(middle_text[1: -1])
#             sorted_text = sorted(middle_text) #lwordist
#             new_list = [char_list[0]] + sorted_text + [char_list[-1]]
#             str_sorted_text = "".join(new_list)
#             result.append(str_sorted_text)
#         else: 
#             result.append(word)
#     print(" ".join(result))
#     return " ".join(result)

# # 1. make a list of words: split()
# # 2. access in a loop, if len is > 2, slice 1:-1
# # 3. sliced word sorted() 
# # 4. reassemble 1, sorted ,-1
# # 5. add to a new list, turn back into string 

# jbelmu("hello world") 
# # "hello wlord"
# jbelmu("freecodecamp is my favorite place to learn to code")
# #"faccdeeemorp is my faiortve pacle to laern to cdoe"
