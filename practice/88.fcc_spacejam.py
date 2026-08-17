https://www.freecodecamp.org/learn/daily-coding-challenge/08-14

- str.strip()은 앞, 뒤 공백만 제거한다. (JS trim 아님 주의)
- str.replace(old, new)는 old를 new로 대체해준다.
- str.split() -> 인자를 주지 않으면 모든 공백을 자동으로 처리한 리스트를 만들어준다.
- 2-1 에서 replace("", "  ") 공백 없음을 두개의 공백으로 대체하니, 문장의 맨 앞, 뒤에도 공백을 넣어버리는 문제 발생. strip()으로 제거해줌.

- 2-2 에서 str을 리스트로 만들 때 list(str) 으로 바로 형변환 해버리고, 두 공백에 "  ".join(list) 해서 str 으로 만든다. 



def space_jam(s):
# 1. clean s : strip() -> replace(), upper() 
    clean_s = s.replace(" ", "").upper()

#2. manipulating
# 2-1.strip, replace 
    r = clean_s.replace("", "  ").strip()
    print(r)

# 2-2.list() / "  ".join() 
    r1 = list(clean_s)
    r2 ="  ".join(r)
    return r2
    
space_jam("   free   Code   Camp   ") #
space_jam("C@t$ & D0g$")





    # uppercase : upper() 
 
    # r = list("abcd")
    # print(r)
    # print("".join(r))
