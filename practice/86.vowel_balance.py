https://www.freecodecamp.org/learn/daily-coding-challenge/08-11

- // 몫 연산자 Floor division/ Integer Division. 정수 인덱스 값 


def is_balanced(s):
    clean_s = s.lower()
    half_idx = len(clean_s) // 2
    first_half = clean_s[:half_idx]

    # if len(clean_s) % 2 == 0:
    #     second_half = clean_s[half_idx:]
    # else:
    #     second_half = clean_s[half_idx + 1:]

    # if-else 쓰지 않고 - 로 뒤에서부터 카운팅 가능 
    second_half = clean_s[-half_idx]

    first_cnt = 0
    second_cnt = 0

    for char in first_half:
        if char in "aeiou":
            first_cnt += 1
    for char in second_half:
        if char in "aeiou":
            second_cnt += 1
    return first_cnt == second_cnt