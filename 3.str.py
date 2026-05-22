str.strip() 글자 양 옆 공백제거
str.lstrip, str.rstrip() 왼, 오른쪽 지정 공백 제거

str.strip("-") 글자 양쪽 끝의 기호만 제거할 때 
str.replace("-", "") 글자 양끝, 중간 모두 대체해버림 

str.split("separator")은 앞뒤, 중간 공백을 다 제거한 깔끔한 리스트를 만들어준다. 구분자는 엑셀에서 문자열 나누기 할 떄와 같다. 
"".join(list)는 요소들 사이에 언더바를 넣어 문자열로 합쳐준다. 
"_".join(list) 여기서 list 요소는 int일 수 없다. str이어야 한다. 

str.startswith("조건str") 조건문에서 문자열이 특정 문자로 시작하는지 불리언으로 리턴
str.endswith("조건str") 
str.endswith(("조건str1", "조건str2", "조건str3"))은 튜플을 인자로 받으면 내부적으로 or 연산을 해준다. 

str.lower() 소문자로 바꿈
str.upper() 대문자로 바꿈
str.title() 첫 글자만 대문자로 변경, 곡 제목같은 경우

str.isdigit() 숫자만 전화번호
str.isalpha() 알파벳으로만 이름, 유니코드 - 한글도 인식함
str.isalnum() 글자나 숫자로만 alpha-numeric 유저네임


sanitising 
사용자 업로드 파일에 공백이 많아 시스템 오류를 유발할 수 있음 공백은 언더바로 교체해 통일
print("_".join(['my', 'resume', '2026.pdf']))
=======================================================================

file_names = [
    "my   resume   2026.pdf",
    " vacation   photo .jpg",
    "final   project   report.docx"
]
# strip() 쓰지 않아도 str.split() 하니 리스트에 공백 없이 들어감 
stripped_result = [data.split() for data in file_names]
# print(stripped_result)
result = ["_".join(data) for data in stripped_result]
# print(result)

print(["_".join(data.split()) for data in file_names])

str.split()은 앞뒤, 중간 공백을 다 제거한 깔끔한 리스트를 만들어준다. 
str.join(list)는 요소들 사이에 언더바를 넣어 문자열로 합쳐준다.  


예시: 단어 사이에 하이픈이 들어간 데이터라면?
data = "--- Hello-World ---"

print(data.replace("-", ""))
# 결과: " HelloWorld "  <-- 중간의 하이픈까지 싹 다 지워져서 단어가 붙어버림!
print(data.strip("-")) 양 옆만 지정해서 지우는 strip()이 적합



서버 로그 파일에서 이미지 소스 분류하기
정상적인 이미지 파일만 url로 만들고 아닌 것은 invalid로 처리함 
정제 조건:앞문: secure_ 로 시작해야 안전한 파일입니다. 
(startswith)뒷문: .jpg, .png, .gif 중 하나로 끝나는 이미지 파일이어야 합니다. 
(endswith)두 조건 모두 만족(and)하면 이름을 그대로 유지합니다.
하나라도 만족하지 못하면 "invalid" 로 변경합니다.
['secure_avatar.jpg', 'invalid', 'invalid', 'invalid', 'secure_logo.gif']


files = [
    "secure_avatar.jpg",   # 1번
    "unsafe_banner.png",   # 2번
    "secure_invoice.pdf",  # 3번
    "ftp_backup.zip",      # 4번
    "secure_logo.gif"      # 5번
]

# print(files[1].startswith("secure")) True False 리턴

# print([data if data.startswith("secure") and (data.endswith("jpg") 
# or data.endswith("png") or data.endswith("gif")) else "invalid" for data in files])

# str.endswith(조건str)은 튜플을 인자로 받으면 내부적으로 or 연산을 해준다. 
print([data if data.startswith("secure") and data.endswith(("jpg", "png", "gif")) 
else "invalid" for data in files])

"회원가입 데이터 유효성 검사 봇" 문제
"사용자가 회원가입 폼에 규격에 맞게 잘 입력했나?"를 검증(Validation)할 때 매일 쓰이는 핵심 함수

raw_users = [
    {"username": "pythoner123", "name": "홍길동", "phone": "01012345678"},  # 1번
    {"username": "user!", "name": "Kim", "phone": "01099998888"},         # 2번
    {"username": "coder99", "name": "이순신12", "phone": "01055556666"},   # 3번
    {"username": "admin", "name": "James", "phone": "010-1111-2222"}      # 4번
]

비즈니스 검증 규칙 (중요):username (아이디): 특수문자가 섞이면 안 되므로, 오직 알파벳과 숫자로만 이루어져야 합니다. (isalnum)
name (이름): 이름에 숫자가 섞이면 안 되므로, 오직 글자(한글/영어)로만 이루어져야 합니다. (isalpha)
phone (전화번호): 하이픈 없이 오직 숫자로만 깔끔하게 입력되어야 합니다. (isdigit)
['Pass', 'Fail', 'Fail', 'Fail']

result = ["Pass" if data["username"].isalnum() and data["name"].isalpha() and data["phone"].isdigit() else "Fail" for data in raw_users]
print(result)

