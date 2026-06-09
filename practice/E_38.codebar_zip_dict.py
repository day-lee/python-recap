def warmup_question(user_emails: list[str], raw_scores: list[int]) -> dict[str, int]:
    """ codebar 
    Marketing Campaign Score Matcher

    - Scenario: The marketing team has exported user emails and campaign participation scores 
                as two separate parallel lists. You need to align and consolidate this data 
                into a single dictionary structure before saving it to the backend database.
    - email should be lowercase 
    - dict comprehension  

    - Execution Example:
        warmup_question(["Alex@Gmail.com", "userB@company.com"], [95, 80])
        
    - Expected Output:
        {'alex@gmail.com': 95, 'userb@company.com': 80}
    """
    # Tell your coach which built-in function and string method you will combine 
    # inside the comprehension, then type it out!

    pass








           
    # - Requirements:
    #     1. Pair the `user_emails` list and the `raw_scores` list 1:1 and iterate through them.
    #     2. Ensure all email addresses are normalized by converting them completely to 'lowercase'.
    #     3. Construct and return a dictionary where the lowercase email serves as the Key 
    #        and the raw score serves as the Value.
    #     4. Implement this core mapping logic strictly inside a single-line 'Dictionary Comprehension'.

    # r = {name.lower(): score for name, score in zip(user_emails, raw_scores)}
    # print(r)

    # from itertools import zip_longest 
    # print(list(zip_longest(user_emails, raw_scores, fillvalue="_") ))
    # return { email.lower(): score for email, score in zip(user_emails, raw_scores)}
        
        
print(warmup_question(["Alex@Gmail.com", "userB@company.com"], [95, 80]))

print(warmup_question(["Alex@Gmail.com", "userB@company.com"], [95, 80, 100])) # itertools zip_longest fillvalue 케이스 
