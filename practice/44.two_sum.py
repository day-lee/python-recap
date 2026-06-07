
def isPalindrome(s: str) -> bool:
    # print(s.replace(" ", "").lower())
    clean_str =  "".join([char for char in s if char.isalnum() ]).lower()
    print(clean_str)
    for i in range(round(len(clean_str) / 2)):
        print(f"start {clean_str[i]}")
        print(f"end: {clean_str[len(clean_str) - 1 -i]}")
        
        if clean_str[i] == clean_str[len(clean_str) - 1 -i]:
            continue
        else: 
            return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
