"""
[베이직 문제 3탄: 여러 주소록의 중복 이름 제거하기]

여러 개의 주소록(리스트)을 한 번에 입력받아서, 
중복된 이름을 모두 제거하고 유일한 이름만 정렬된 리스트로 반환하는 함수를 만드세요.

요구사항:
1. 가변 인자(*args)를 사용하여 여러 개의 리스트를 한 번에 입력받으세요.
2. 반복문(for)을 사용해 입력받은 리스트들을 하나의 세트(set)에 합치세요.
   (힌트: 세트의 .update() 메서드를 사용하면 편리합니다.)
3. 중복이 제거된 결과를 다시 '오름차순 정렬된 리스트'로 반환하세요.
"""
# def merge_and_sort_names(*args):
#     unique_names = set()
    
#     # 1. 가변 인자 args를 반복문으로 순회하며 unique_names에 추가해보세요.
#     # 2. 마지막에 정렬된 리스트로 변환하여 반환하세요.
#     pass

def merge_and_sort_names(*args):
    unique_names = set()
   
    for item in args:
       # update()를 사용하면 여러 리스트를 통째로 합쳐준다. add()는 딱 하나의 데이터 추가할 때. 
       unique_names.update(item)
    # set는 iterable 이라서 sorted() 첫인자로 바로 들어간다. 리스트로 바꿀 필요 없음 
    result = sorted(unique_names)
    return result

# ==============================================================================
# [테스트 실행 코드]
# ==============================================================================
if __name__ == "__main__":
    group_a = ["Kim", "Lee", "Park"]
    group_b = ["Lee", "Choi"]
    group_c = ["Park", "Jung", "Kim"]

    # 가변 인자이므로 여러 리스트를 원하는 만큼 던질 수 있습니다.
    result = merge_and_sort_names(group_a, group_b, group_c)
    print(result)
    
    # 예상 출력 결과 (중복이 제거되고 알파벳 순으로 정렬되어야 합니다):
    # ['Choi', 'Jung', 'Kim', 'Lee', 'Park']
