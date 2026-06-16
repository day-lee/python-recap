def letter_count_i(str_param: str) -> str:
    """
    Coderbyte: Letter Count I

    Take the space-separated string parameter being passed and return the first word 
    with the greatest number of repeated letters. 
    If there are no words with repeating letters, return the string "-1".

    [Requirements]
    1. The input string consists of multiple words separated by spaces.
    2. Count how many times a character repeats within each individual word.
       (e.g., "greatest" -> 'e' appears twice, 't' appears twice, so the max repeat count is 2)
    3. If there is a tie for the highest repeat count, return the first word that appears in the sentence.
    4. If no words contain any repeating letters (all characters appear only once), return the string "-1".
    5. Punctuation marks (,.!) can either be included or ignored; 
       however, it is safer to filter them out and check only alphabetic characters.

    Args:
        str_param (str): A space-separated string of English words.

    Returns:
        str: The matching word, or the string "-1" if no repeating letters are found.

    Examples:
        >>> letter_count_i("Hello apple pie")
        'Hello' ('l' appears twice, 'p' appears twice, but 'Hello' comes first)
        >>> letter_count_i("No words here")
        '-1' (No words contain any repeating letters)
        >>> letter_count_i("Today, is the greatest day!")
        'greatest' ('e' and 't' both repeat twice)
    """
    pass 











    """모범 답안 dict에서 값의 max를 구하려면 max(dict.values())
    max_word = "-1"
    max_count = 1

    if not str_param: # "" 빈 문자열은 false로 평가됨  
        return "-1"

    for word in str_param.split():
        count = {}. 
        for char in word.lower():
            if char.isalpha():
                count[char] = count.get(char, 0) + 1 
        if not count: # 단어에 알파벳이 없는 경우 대비, empty then next word 
            continue 
        temp_count = max(count.values())
        if temp_count > max_count:
            max_count = temp_count
            max_word = word 

    return max_word
    """
    # make a list, loop to access each word, and char, 
    # count each char, only store max count {word: max_count, .. }
    # var max_word, max_count in the loop to compare among words 
     










    """
    from collections import Counter
    str_list = str_param.lower().split()
    result_word = "-1"
    max_repeat_count = 1 

    for word in str_list:
        char_count = Counter(word)

        # char_count = {}
        # for char in word:
        #     char_count[char] = char_count.get(char, 0) + 1 

        current_max = max(char_count.values())
        print(current_max)
        if current_max > max_repeat_count:
            max_repeat_count = current_max
            result_word = word      

    return result_word
    """
# 테스트 실행 코드 (구현 후 주석을 해제해서 확인해보세요)
print(letter_count_i("Hello apple pie"))  # Expected: "Hello"
print(letter_count_i("!!! apple pie!!! "))  # Expected: "apple"
print(letter_count_i("No words her"))    # Expected: "-1"
