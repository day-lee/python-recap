"""
    Follow-up:
    1. 왜 read()를 사용하면 안 되는가? 
        -> read() readlines()는 데이터를 한번에 메모리 RAM 공간에 올리려고 시도해서 OOM 에러가 난다. 

    2. generator가 이 문제에서 어떤 역할을 하는가? 
        -> f 파일 객체는 그 자체로 Generator(iterator)처럼 동작한다. for line in f 를 하면 내부적으로 next()를 호출하며 현재 읽어야할 딱 한줄만 메모리에 로드한다. yield를 통해 한줄만 전달하고 메모리 비운다. 

    3. 파일이 존재하지 않는다면 어떻게 처리할 것인가? 
        -> 로그를 남기고, 예외(FileNotFoundError)처리를 한다. 

    4. 파일 encoding을 명시해야 하는 상황은 언제인가? 
        -> OS환경마다 인코딩이 다르고 외국어, 이모지, 특수문자 등 포함되면 UnicodeDecodeError가 발생한다. 따라서 항상 encoding='utf-8'을 명시한다. 

"""
def problem_06_generator_file_processing():
    """
    [Generator + File Handling]

    매우 큰 로그 파일이 있다고 가정한다.

        app.log

    파일의 크기는 50GB이며 다음과 같은 라인이 존재한다.

        INFO User login
        ERROR Database connection failed
        INFO Request completed
        ERROR Timeout
        INFO User logout

    파일 전체를 메모리에 올리지 않고 ERROR가 포함된 라인만
    하나씩 반환하는 generator를 작성하라.

    요구사항:
    - open()을 사용하라.
    - with를 사용하라.
    - yield를 사용하라.
    - read() 또는 readlines()를 사용하지 마라.

    사용 예:

        for line in error_lines("app.log"):
            print(line)

    """
    pass

import os
def log_parser(file_path):

    if not os.path.exists(file_path):
        print('file not found')
        return 

    with open(file_path, mode='r', encoding='utf-8') as f:

        for line in f:
            if 'ERROR' in line:
                yield line.strip()


# 사용 예시
for line in log_parser("appe.log"):
    print(line)

