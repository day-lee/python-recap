# https://www.freecodecamp.org/learn/daily-coding-challenge/11-17

def is_match_zip(fingerprint_a, fingerprint_b):
    a_len = len(fingerprint_a)
    b_len = len(fingerprint_b)

    # early return
    if a_len != b_len:
        print("Early return: length mismatch")
        return False

    diff_str_num = 0
    for a_char, b_char in zip(fingerprint_a, fingerprint_b):
        if a_char != b_char:
            diff_str_num += 1
        

    # print('DIFF', diff_str_num) #3
    # print('A_LENTH', a_len * 0.1) #3.5
    print(diff_str_num <= a_len * 0.1)
    return diff_str_num <= a_len * 0.1


is_match_zip("helloworld", "helloworld") #true
is_match_zip("helloworld", "helloworlds") # false
is_match_zip("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat") #False
    


def is_match(fingerprint_a, fingerprint_b):
    a_len = len(fingerprint_a)
    b_len = len(fingerprint_b)

    # early return
    if a_len != b_len:
        print("Early return: length mismatch")
        return False

    diff_str = ""
    for i, char in enumerate(fingerprint_b):
        if fingerprint_a[i] != char:
            diff_str += char
        
    len_different_str = len(diff_str)

    print('DIFF', len_different_str) #3
    print('A_LENTH', a_len * 0.1) #3.5
    print(len_different_str <= a_len * 0.1)
    return len_different_str <= a_len * 0.1


# is_match("helloworld", "helloworlds")
# is_match("helloworld", "helloworld") 
# is_match("helloworld", "jelloworld")
# is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat")
    
    

