"""
[Senior's Challenge: Member Matching and Variable Data Cleaning]

* Topics: zip_unpacking, list_dict_comprehension, exception, tuple, str, function
* Scenario: You have a 'member name string' and a 'contact tuple list' scraped from two different databases. 
            You need to match these two datasets and merge them into a single, clean dictionary.
"""

def merge_and_clean_profiles(raw_names: str, contact_tuples: list) -> dict:
    """
    Combines a comma-separated string of member names with a list of (phone, email) tuples.
    Clean and refine the data into a dictionary while safely guarding against missing data and errors.

    [Requirements]
    1. Name Cleaning (str):
       - `raw_names` is a single long string (e.g., " alice , bob , , charlie ").
       - Split the string by commas (,) and remove any leading or trailing whitespace.
       - If a split value is an empty string ("") or contains only whitespace, exclude it from the list.

    2. Data Merging & Exception Handling (zip_unpacking & exception):
       - Pair the cleaned name list and `contact_tuples` in order using `zip` or a loop.
       - Note that the name list and the tuple list 'may have different lengths'.
         * No empty values should be generated due to a lack of data on either side during the operation.
         * If the data pairs do not match perfectly, or if an IndexError occurs due to an invalid format 
           inside `contact_tuples`, safely stop processing (break) at that point and return only the 
           results accumulated up to that moment.
       
    3. Output Format (Dictionary Comprehension):
       - The final result must be returned as a dictionary.
         * Key: The member's name converted to uppercase (e.g., "ALICE")
         * Value: A dictionary containing contact details `{"phone": phone_number, "email": email_address}`
       - (Optional Tip) While you can use a standard loop to implement this, utilizing a Dictionary Comprehension 
         for the final stage will make your code look much cleaner and more professional.

    Args:
        raw_names (str): A messy, comma-separated string of names.
        contact_tuples (list): A list of tuples in the form of (phone, email).

    Returns:
        dict: The cleaned and refined member profile dictionary.
    """



    # 빈칸은 isalnum()에서 제외된다. " alice ".isalnum()은 False 
    # raw_names_list = [ name.strip() for name in raw_names.split(",") if name.strip() ]
    # result = {} 
    # for i, name in enumerate(raw_names_list):
    #     try:
    #         contact = contact_tuples[i]
    #         result[name.upper()] = {
    #             "phone": contact[0],
    #             "email": contact[1]
    #         }
    #     except IndexError:
    #         break
        
    # return result


# =====================================================================
# 검증용 테스트 코드 (IDE에서 실행하여 결과를 확인하세요)
# =====================================================================
if __name__ == "__main__":
    # 1. 지저분한 로우 데이터 문자열 (중간에 빈 값 ", ," 도 섞여 있음)
    names_data = " alice , bob , , charlie , david "
    
    # 2. 연락처 데이터 튜플 리스트 (이름은 4개인데 연락처는 3개만 있는 불일치 상황)
    contacts_data = [
        ("010-1234-5678", "alice@test.com"),
        ("010-9999-8888", "bob@test.com"),
        ("010-5555-4444", "charlie@test.com")
    ]

    result = merge_and_clean_profiles(names_data, contacts_data)
    
    print("=== 최종 프로필 정제 결과 ===")
    import pprint
    pprint.pprint(result)
    
    """
    [예상 출력 결과]
    {
        'ALICE': {'email': 'alice@test.com', 'phone': '010-1234-5678'},
        'BOB': {'email': 'bob@test.com', 'phone': '010-9999-8888'},
        'CHARLIE': {'email': 'charlie@test.com', 'phone': '010-5555-4444'}
    }
    
    (연락처가 없는 'david'는 결과에서 안전하게 누락/제외되어야 합니다.)
    """
