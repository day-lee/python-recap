# https://www.freecodecamp.org/learn/daily-coding-challenge/09-22

# isalpha()
# isdigit()
# isalnum()
# 2번이나 제너레이터 표현식이 좋음 

def digits_or_letters(s):

    num_digit = 0
    num_alpha = 0

    for char in s:
        if char.isalpha():
            num_alpha += 1
        if char.isdigit():
            num_digit += 1
    # print(num_digit, num_alpha)

    if num_digit == num_alpha:
        return 'tie'
    elif num_digit > num_alpha:
        return 'digits'
    else:
        return 'letters'

print(digits_or_letters("abc123"))
print(digits_or_letters("H3110 W0R1D"))


def digits_or_letters_2(s):
    num = 0
    for char in s:
        if char.isalpha():
            num += 1
        if char.isdigit():
            num -= 1

    if num > 0:
       return 'letters'
    elif num < 0 :
        return 'digits'
    else:
        return 'tie'

print('_______________________________')
print(digits_or_letters_2("abc123")) # tie
print(digits_or_letters_2("abc123!@#DEF")) # "letters"
print(digits_or_letters_2("1a2b3c4")) # digits



def digits_or_letters_3(s):

    alpha = [char for char in s if char.isalpha()]
    digit = [char for char in s if char.isdigit()]

    num_alpha = len(alpha)
    num_digit = len(digit)

    if num_alpha > num_digit:
        return 'letters'
    elif num_alpha < num_digit:
        return 'digits'
    else:
        return 'tie'


print('_______________________________')
print(digits_or_letters_3("abc123")) # tie
print(digits_or_letters_3("abc123!@#DEF")) # "letters"
print(digits_or_letters_3("1a2b3c4")) # digits


"""
sum(iterable, start=0)

sum(generator_expression)
-> sum((generator_exp)) 여야 할 것 같지만 괄호 생략을 파이썬이 허용해줌 

sum([1 for char in s if char.isalpha()]) 
VS
sum(1 for char in s if char.isalpha())

리스트 컴프리헨션으로 조건에 맞는 모든 1을 모아서 리스트 메모리 공간에 만들어 둔뒤 sum()함수에 넘긴다.
만약 s의 길이가 매우 길다면 순간 메모리 폭발 가능성이 있음 

제너레이터는 리스트를 미리 만들지 않고 sum()함수가 다음 숫자 줘 라고 요청할 때 마다 1을 넘겨준다.
lazy evaluation으로 메모리 폭발이 없고, 성능이 좋다. 

"""
def digits_or_letters_4(s):
    num_alpha = sum(1 for char in s if char.isalpha())
    num_digit = sum(1 for char in s if char.isdigit())

    # print([1 for char in s if char.isdigit()]) #[1, 1, 1, 1]
    
    if num_alpha > num_digit:
        return 'letters'
    elif num_alpha < num_digit:
        return 'digits'
    else:
        return 'tie'

print('_______________________________')
print(digits_or_letters_4("abc123")) # tie
print(digits_or_letters_4("abc123!@#DEF")) # "letters"
print(digits_or_letters_4("1a2b3c4")) # digits