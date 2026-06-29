def question_14():
    """
    [14번 문제] 타겟 고객 세트 연산 및 등급 분류 

    - 상황: 신작 게임 출시를 앞두고 VIP 유저와 길드 마스터 유저 명단을 확보했습니다.
    - 요구사항:
        1. VIP이면서 '동시에' 길드 마스터인 핵심 유저에게는 "LEGEND" 등급을 부여하세요.
        2. 둘 중 '한 곳에만' 속한 유저에게는 "HERO" 등급을 부여하세요.
        3. 최종 결과는 {유저ID: 등급} 형태의 딕셔너리로 만드세요.
    - 출력 예시: {'user1': 'LEGEND', 'user3': 'LEGEND', 'user2': 'HERO', 'user4': 'HERO'}
               (딕셔너리 특성상 순서는 무관합니다)
    """
    vip_users = {"user1", "user2", "user3"}
    guild_masters = {"user3", "user4", "user1"}

    pass













    """ 모범 답안
    set 연산자를 활용하기 합집합, 교집합 
    #1
    result_dict = {} 
    legends = vip_users & guild_masters 
    heros = vip_users ^ guild_masters 

    for user in legends:
        result_dict[user] = "LEGEND"
    for user in heros:
        result_dict[user] = "HERO"

    # 모범 답안 2 
    all_users = vip_users | guild_masters
    return {user: "LEGEND" if user in vip_users and user in guild_masters else "HERO" for user in all_users}
    """

    # 이 방법은 형변환이 무의미하게 자주 일어남 
    # new_list = list(vip_users) + list(guild_masters)
    # result_dict = {}

    # for user in set(new_list):
    #     if user in vip_users and user in guild_masters:
    #         result_dict[user] = "LEGEND"
    #     elif user in vip_users or user in guild_masters:
    #         result_dict[user] = "HERO"

    print(f"14번 결과: {result_dict}")
    return result_dict

print(question_14())



