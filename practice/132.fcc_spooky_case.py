# https://www.freecodecamp.org/learn/daily-coding-challenge/10-31
- Ternary Operator, Conditional Expression
- flipping boolean 의 경우 'should_capitalised = not should_capitalised' 처럼 not을 붙여주면 한줄로 핸들링 할 수 있음 


def spookify_1(boo):
    should_capitalised = True
    result_str = ''
    for char in boo:
        if char.isalpha():
            if should_capitalised:
                result_str += char.upper()
            else:
                result_str += char.lower()
            should_capitalised = not should_capitalised
        else:
            result_str += '~'        
    return result_str

spookify_1("hello_world")
spookify_1("TRICK-or-TREAT")


def spookify_2(boo):
    should_capitalised = True
    result_str = ''
    for char in boo:
        if char.isalpha():
            # ternary operator
            result_str += char.upper() if should_capitalised else char.lower()
            should_capitalised = not should_capitalised
        else:
            result_str += '~'
    print(result_str)
    return result_str

spookify_2("hello_world")
spookify_2("TRICK-or-TREAT")




