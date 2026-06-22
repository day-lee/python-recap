
"""
Live coding communication

1. Aligning Expectations: 
"I'll read the instruction out loud to align on the requirements..."

2.  Interactive Reading & Keyword Spotting:
"...Wrap the parsing logic in a try-except block... [PAUSE] Ah, this is for handling malformed logs safely so the function doesn't crash."

3. Validation & Edge Case:
"Looking at the examples, what if the input list is empty? Should it return an empty dict?"

4.  Intent & Approach:
"Great. Now, let me explain my approach before I start coding..."

... coding, thinking aloud

5. Complexity & Trade-off Discussion 

"""
def validate_and_filter_users(user_data):
    """
    Parses a list of user raw data tuples, validates their format, 
    and returns a filtered dictionary of active administrators.

    Each input element is a tuple: (username, role, status) 
    For example: ("alice ", " ADMIN ", "active")

    Requirements:
    1. String Sanitization: Strip all trailing and leading whitespaces from 
       the username and role. Convert the role to uppercase.
    2. Exception Handling: If an entry is not a tuple or does not contain 
       exactly 3 elements, catch the `ValueError` or `TypeError` safely, 
       skip that invalid entry, and continue processing.
    3. Filtering & Comprehension: Use a dictionary comprehension to build 
       the final result. Include the user ONLY if their cleaned role is "ADMIN" 
       and their status is "active". -> 굳이 컴프리헨션으로 쓰지 않아도 됨. 불필요함 
    4. Dictionary Output: The resulting dictionary must have the cleaned 
       username as the key and a boolean value `True` as the value.

    0. early return if no argument with len()    
    1. for loop, tuple unpacking? 
    2. username, role: strip(), only role - upper()
    3. try -catch : isinstance(v, tuple), len(), `ValueError` or `TypeError` , continue 
    4. if condition,  role is "ADMIN" status is "active" - dictionary comprehension 
        key- username, True

    Args:
        user_data (list of tuples): A list containing raw user information.
            Example: 
            1. 
            [
                ("alice ", " ADMIN ", "active"),
                ("bob", "user", "active"),
                ("charlie", "admin", "inactive"),
                ("corrupted_data_line"),  # Invalid: not a 3-element tuple
                ("david", "ADMIN", "active"),
                ()
            ]
            2. 
            edge case 
            [] 

    Returns:
        dict: A dictionary of validated active administrators.
            Example: {"alice": True, "david": True}
    """
    
    """모범답안 
    if not user_data:
        return {}
    
    result = {}

    for data in user_data:
        try:
            # 언패킹 시도, 여기서 3개가 아니거나, 순회가 불가능하면 에러 발생
            name, role, status = data
            name = name.strip() 
            role = role.strip().upper() 
            if role == "ADMIN" and status == "active":
                result[name] = True 

            # 이 구문은 필요가 없음. 위에서 에러나는거 잡는게 목적  
            # if not(len(data) == 3 and isinstance(data, tuple)): 
            #     continue
        except (TypeError, ValueError):
            continue 
    # result = { name: True for name, role, status in new_list if role == "ADMIN" and status == "active"}
    return result 
    """

    # codebar communication 1 - live coding with coach Amazonia
    # # TODO: Explain your logic to the coach out loud, then implement the code here
    # # 0. early return if no argument with len()    
    # # print(user_data)
    # result = {}
    # new_list = []
    # if len(user_data) == 0:
    #     return {}
    # # 1. for loop, tuple unpacking? 
    # for data in user_data:
    # # 3. try -except : isinstance(v, tuple), len(), `ValueError` or `TypeError` , continue 
    #     try: 
    #         # print(type(data))
    #         if not isinstance(data, tuple):
    #             # print(data, type(data))
    #             raise TypeError("It should be tuple type")
    #         if len(data) != 3:
    #             # print(data, len(data))
    #             raise ValueError("It should contain 3 elements")
    #     except (TypeError, ValueError) as e: 
    #         continue
    #         # print(f"except: {e}")
    # # 2. username, role: strip(), only role - upper()
        
    #     name, role, status = data
    #     # print((name, role, status))
    #     new_user = (name.strip(), role.strip().upper(), status)
    #     print(f"new_user=====: {new_user}")
    #     new_list.append(new_user)
    # # print({name: True for name, role, status in new_list if role == "ADMIN" and status == "active" })
    # return {name: True for name, role, status in new_list if role == "ADMIN" and status == "active" }
    # # print(new_list)
    # #     if new_user[1] == "ADMIN" and new_user[2] == "active":
    # #         result[new_user[0]] = True
    # # print(result)

    #     # {new_user[0]: True for new_user in ... if new_user[1] == "ADMIN" and new_user[2] == "active" }
    # # 4. if condition,  role is "ADMIN" status is "active" - dictionary comprehension 
    # #     key- username, True


print(validate_and_filter_users([
                # ("alice ", " ADMIN ", "active", "feb", "mon"),
                ("alice ", " ADMIN ", "active"),
                ("bob", "user", "active"),
                ("charlie", "admin", "inactive"),
                ("corrupted_data_line"),  # Invalid: not a 3-element tuple
                ( "david", "ADMIN", "active"), # invalid: length 4 
                ("david", "ADMIN", "active"),
                ("david", "ADMIN",),
                1
            ]))


# validate_and_filter_users([])

# validate_and_filter_users([1, 2])








