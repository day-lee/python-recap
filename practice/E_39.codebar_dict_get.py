def question_23(min_score: int, *user_records, **regional_bonus) -> dict[str, int]:
    """[Question 23] Marketing Campaign Score Filter & Bonus Calculator
    - Scenario:
        Aggregate global marketing event results, calculate final scores by applying 
        region-specific bonuses, and filter out candidates who do not meet a minimum 
        score threshold.
    - Requirements:
        1. The variable positional arguments `*user_records` accepts an arbitrary 
           number of 'tuples', where each tuple represents (name: str, region: str, base_score: int).
           e.g., ("Tom", "UK", 75), ("Sara", "US", 90)
        2. The keyword arguments `**regional_bonus` maps region codes to their 
           respective bonus point values (int).
           e.g., UK=10, US=5
        3. Iterate through `*user_records` and calculate the final score for each user. 
           The final score is computed as `base_score + regional_bonus_points`. 
           If a user's region does not exist in `regional_bonus`, default the bonus points to 0.
        4. Filter and retain only those users whose calculated final score is greater 
           than or equal to `min_score`.
        5. Return a dictionary where the qualified user's name serves as the Key 
           and their final score serves as the Value.
        6. Implement this entire extraction, calculation, filtration, and composition 
           logic strictly inside a single-line 'Dictionary Comprehension'.
    - Execution Example:
        question_23(80, ("Tom", "UK", 75), ("Sara", "US", 90), ("Alex", "FR", 70), UK=10, US=5)
         
    - Expected Output:
        {'Tom': 85, 'Sara': 95}
        (Explanation: Tom gets 75+10=85 and passes. Sara gets 90+5=95 and passes. 
                      Alex gets 70+0=70, which is below the min_score of 80, so he is excluded.)
    # Discuss inline tuple unpacking and using the .get() method inside a comprehension 
    # with your coach before typing your solution!
    """

    pass











    """ 바다표범 연산자 모범답안
      동일 연산이 두번 일어나는 것을 방지하기 위해 파이썬 3.8부터 Walrus operator 바다표범 연상자가 나옴. 
    r = {
        name: final_score
        for name, region, score in user_records
        if (final_score := score + regional_bonus.get(region, 0)) >= min_score }
    print(r)
    return r
    """
 
    # r = { name: score + regional_bonus.get(region, 0) for name, region, score in user_records if score + regional_bonus.get(region, 0) >= min_score }
    # print(r)
    # my_result = {}
    # for name, region, score in user_records:
    #     final_score = score + regional_bonus.get(region, 0)
    #     print(final_score)
    #     if final_score >= min_score:
    #         my_result[name] = final_score
    # one liner
    # return { name: score + regional_bonus.get(region, 0) for name, region, score in user_records if score + regional_bonus.get(region, 0)>= min_score }      
# 3 함수 외부 테스트 실행 
print(question_23(80, ("Tom", "UK", 75), ("Sara", "US", 90), ("Alex", "FR", 70), UK=10, US=5))
