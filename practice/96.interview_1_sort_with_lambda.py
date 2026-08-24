- timsort는 O(NlongN) 이므로 항상 믿고 빠르게 정렬할 수 있다.

- key인자는 callable을 인자로 받음. 호출 가능한 객체. ()를 붙여 호출하면 안됨.
- 키는 주로 anonymous function인 람다 함수를 받는다.
- fn x => x + 1
- lambda x: x + 1

- len()함수를 key로 전달할 때.
words = ['apple', 'banana', 'kiwi', 'watermelon']
r = sorted(words, key=len) #-> len() 아님 주의 
print(r)  # 출력: ['kiwi', 'apple', 'banana', 'watermelon'] length 순서대로 나옴 

- 'reverse=True' 내림차순이 desc. 표시 필요함. - 마이너스 붙이면 내림차순 
- 'reverse=False' 오름차순이 asc 기본값


def problem_01_sort_with_lambda(employees):
    """
    [Lambda]

    다음과 같은 employee 데이터가 주어진다.

        employees = [
            {"name": "Alice", "salary": 70000},
            {"name": "Bob", "salary": 50000},
            {"name": "Charlie", "salary": 90000},
        ]

    salary가 높은 순서대로 정렬한 새로운 리스트를 반환하라.

    조건:
    - sorted()를 사용하라.
    - lambda를 사용하여 정렬 기준을 지정하라.
    - 원본 employees는 변경하지 않아야 한다.

    Follow-up:
    1. salary가 낮은 순서대로 정렬하려면?
    2. salary가 같은 경우 name을 알파벳순으로 정렬하려면?
    3. lambda를 사용하지 않고 구현한다면 어떻게 할 것인가?
    """
    pass

employees = [
            {"name": "Jack", "salary": 70000},
            {"name": "Alice", "salary": 70000},
            {"name": "Bob", "salary": 50000},
            {"name": "Charlie", "salary": 90000},
        ]

# 높은 순 정렬
# 앞에 - 마이너스 붙이면 내림차순됨 
def problem_01_sort_with_lambda_1(employees):
    r = sorted(employees, key=lambda x:x['salary'], reverse=True)
    # r = sorted(employees, key=lambda x:-x['salary']) #가독성 안좋아서 reverse=True 선호 
    print(r)



# 낮은 순 정렬 
def problem_01_sort_with_lambda_2(employees):
    print(sorted(employees, key=lambda x: x['salary']))



# 동점자 두 가지 정렬 기준: 튜플에 순서대로 넣어주고, 마이너스 기호 사용
def problem_01_sort_with_lambda_3(employees):
    print(sorted(employees, key= lambda x:(-x['salary'], x['name'])))



# 만약 salary는 낮은 순, name은 뒤에서부터 정렬하고싶다면?
# - 마이너스 기호가 알파벳에는 사용할 수 없다. 
# 원래 -를 붙이면 내림차순이지만, 이름은 알파벳인 관계로 한번 더 뒤집어준다. 
# 전체에 reverse=True를 주고 숫자인 salary는 -를 붙여서 내림차순, name은 오름차순 정렬 
def problem_01_sort_with_lambda_4(employees):
    print(sorted(employees, key=lambda x: (-x['salary'], x['name']), reverse=True))


def order(x):
    return (-x['salary'], x['name'])


# 람다를 사용하지 않고 구현
from operator import itemgetter
def problem_01_sort_with_lambda_5(employees):
    r = sorted(employees, key=itemgetter('salary'), reverse=True)
    print(r)
    # r = sorted(employees, key=itemgetter('salary', 'name')) # 동점자 처리 연봉 오름순, 이름 오름순

problem_01_sort_with_lambda_1(employees)
problem_01_sort_with_lambda_2(employees)
problem_01_sort_with_lambda_3(employees)
problem_01_sort_with_lambda_4(employees)
problem_01_sort_with_lambda_5(employees)





