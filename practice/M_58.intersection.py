""" coderbyte
Find Intersection

Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.

"""

def find_intersection(strArr):
  pass 

  """ 최적화 답안
  기준 리스트를 세트로 변환한 뒤, 두번째 리스트 순회하며 in 으로 포함여부 체크 
  set 과 in 을 이용해서 연산을 빠르게함. 리스트는 선형 탐색이라 성능 낮음 
  
  # 1. 첫 리스트를 정수형 해시 세트로 변환해서 탐색 속도 높힘 
  # split후 공백 포함될 수 있으니 int() 변환 
  set1 = set(int(num) for num in strArr[0].split(",")) 
  # 2. 두번째 리스트 순회하며 set1에 존재하는지 확인 - 교집합 
  # 이미 주어진 리스트가 정렬되어 있으므로 순서대로 검사하면 이미 정렬된 상태 
  intersection = [num.strip() for num in strArr[1].split(",") if int(num) in set1]
  # 3. 예외 처리 및 결과 반환 
  if not intersection:
    return "false"
  return ",".join(intersection)
  """

  """ 내 답안 
  # make a combined list +
    combined_list = strArr[0].split(",") + strArr[1].split(",")
  # iterate to crate counter hash dict - occurence
    counter = {}
    result_list = []
    for num in combined_list:
      int_num = int(num)
      counter[int_num] = counter.get(int_num, 0) + 1
  # if, value >= 2 then make a list
  # if len of result list is 0, False 
    for key, value in counter.items():
      if value >= 2:
        result_list.append(str(key)) # type 
    if len(result_list) == 0:
      return "false" # return the string false.
    # sort the list
    result_list.sort(reverse=False, key=int)
    # turn into string
    return ",".join(result_list)
  """
# keep this function call here 
print(find_intersection(["1, 5, 6, 7, 10, 11, 12", "5, 6, 8, 11, 17"] )) # 5,6,11
print(find_intersection(["1, 2, 4, 5, 6, 9", "2, 3, 4, 8, 10"])) #2, 4
print(find_intersection(["5, 6, 9, 11, 12, 16", "4, 6, 7, 11, 16"])) #6,11,16
