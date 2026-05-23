
exception runtime error
x = 2
assert x > 10, "x is not greater than 10" # debugging tool 



try:
    num = int(input("please enter a number btw 5 to 10: "))
    if num < 5 or num > 10:
        raise Exception
except:
    print('error: please enter 5 - 10')
finally: 
    print("program finished")



print(1/0) #ZeroDivisionError: division by zero

try:
    print(1/0)
except:
    print("cannot divide by zero")

파이썬 예외(exception)은 최상위 클래스인 Exception을 상속받아야한다.
Exception 클래스를 상속받았기 때문에, 클래스 내부에 아무 내용없이 pass 키워드만 적어도 raise 같이 예외를 발생 시키는 기능을 사용할 수 있다. 
class ValueTooLow(Exception):
    pass
class ValueTooHigh(Exception):
    pass
try:
    input = int(input("enter a number btw 5 to 10: "))
    if input < 5:
        raise ValueTooLow("the value is too low!")
    if input > 10:
        raise ValueTooHigh("the value is too high!")
# 별도의 예외 처리마다 except 블록을 만들어 줘야함. 발생한 에러 객체를 e라는 변수로 받음        
except ValueTooLow as e:
    print(e)
except ValueTooHigh as e:
    print(e)
except ValueError:
    print("please enter numbers only")



import math
class InvalidLength(Exception):
    pass
try:
    input = int(input("input the duration of a song of their choice in seconds: "))
    if input < 0:
        raise InvalidLength("Invalid input for song duration")
except InvalidLength as e:
    print(e)
except:
    print("ERROR: enter only numbers")    
else:
    print(math.trunc(input / 60), "mins")
math.trunc는 소수점 아래를 잘라내고 정수만 반환함 