"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 
Input: n = 3
Output: ["1","2","Fizz"]

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

"""
def fizzBuzz(n: int) -> list[str]:
    pass (문자열 더하기 방식으로 풀기)












""" 모범 답안

# 내 답안
def fizzBuzz(n: int) -> list[str]:
    result = []
    # range(1, n+1), 1부터 시작하기 위해 n 이 아니라 1로 시작한다. 종료는 +1해주어 길이 맞춰준다. 
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")        
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))
    return result 

# AI 답안
    def fizzBuzz(n: int) -> list[str]:
        result = []
        for i in range(1, n+1):
            word = ""
            if i % 3 == 0:
                word += "Fizz"
            if i % 5 == 0:
                word += "Buzz"
            if not word:
                word = str(i)
            result.append(word)
        return result
        # return

"""
print(fizzBuzz(3)) # ["1","2","Fizz"]
print(fizzBuzz(5)) # ["1","2","Fizz","4","Buzz"]     
print(fizzBuzz(15)) # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]        
