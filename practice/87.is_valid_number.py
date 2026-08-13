- string에 lower()를 적용하면 대문자를 소문자로 바꿔준다.
- isAlpha()를 쓰지 않아도 된다.
- '20abcDF'.lower()

base36_list = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

def is_valid_number(n, base): 
    base_range_list = base36_list[:base]
    for char in n.upper():
        if char not in base_range_list:
            return False
    return True

print(is_valid_number("AbC", 16)) 
print(is_valid_number("10101", 2))
print(is_valid_number("10101", 2))