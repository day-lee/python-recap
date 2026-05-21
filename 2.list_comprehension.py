my_list = [i for i in range(5)]
print(my_list)

my_even_list = [i for i in range(5) if i % 2 == 0]
print(my_even_list)

fruits = ["banana", "apple", "strawberry"]
fave = [fruit for fruit in fruits if fruit == "strawberry"]
print(fave)

my_dict = {"name": "misty", "type": "cat", "age": 12, "isFemale": True}
print(my_dict.get("name"))

for data in my_dict:
    print(my_dict.get(data))

info = [my_dict.get(data) for data in my_dict]
print(info)

my_dict["color"] = "black" # This is the correct way to add a key-value pair to a dictionary

info2 = {my_dict.get(data): data for data in my_dict}
print(info2)

fruits = ["banana", "apple", "strawberry"]
# result = [ "protein" if fruit == "banana" else "fruity" for fruit in fruits]

print(result)
if else 문으로 작성할 때는 표현식 expression과 if else가 for loop 앞에 위치한다.


words = ["apple", "banana", "kiwi", "grape", "melon", "plum"]
result = [word if len(word) >= 5 else "short" for word in words ]
print(result)

2차원 리스트 평탄화 - 중첩 루프이용 - 중첩일 때는 맨 마지막 줄만 맨 앞으로 보낸다. 
matrix = [[1, 2], [3, 4], [5, 6]]
result = [j for i in matrix for j in i]
print(result)

result = []
for i in matrix:
    for j in i:
        result.append(j)
print(result)

matrix = [[1, 2], [3, 4], [5, 6]]
result = [j for i in matrix for j in i if j % 2 == 0]
print(result)

matrix = [[1, 2], [3, 4], [5, 6]]
result = [j if j % 2 == 0 else "odd" for i in matrix for j in i ]
print(result)