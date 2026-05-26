Python Standard Library

json.dumps(dict) 직렬화 
json.loads(json_str) 역직렬화. 파이썬 딕셔너리로 바꿀 때 

datetime.date.today()

os.getenv("DB_PASSWORD")

random.randint(1, 10)
random.choice(list)

time.sleep(1)

traceback.format_exc() 에러 히스토리 문자열 추출

operator.itemgetter
list.sort(key=itemgetter(1)) 람다를 대체해서 데이터 정렬 할 때 

itertools.zip_longest 길이가 다른 두 리스트 묶을 때, zip()은 짧은 리스트 기준으로 잘라서 데이터 유실 우료가 있지만, zip_longest는 빈 곳을 지정 값으로 채움

glob
glob.glob("*.txt") 현재 폴더의 모든 텍스트 파일 리스트로 긁어모음

shutil 파일이나 폴더를 복사, 이동, 삭제시 사용

sys 파이썬 인터프리터 제어 모듈. 
sys.exit()
sys.argv

itertools.combination 리스트에서 순서 없이 가능한 원소 조합 구해줌 


urllib -> requests, httpx 
pickle -> json 
threading -> 동시성 asyncio, multiprocessing 
webbrowser -> 자동화 스크립트. 브라우저 강제로 열어서 url로 이동할 때 
