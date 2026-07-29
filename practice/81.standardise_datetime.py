from datetime import datetime


def standardize_dates(raw_dates):
    """
    Standardize a list of heterogeneous date strings into a unified format.

    In data engineering, upstream sources often send timestamps in various formats.
    Your task is to parse these mixed formats and convert them into a single
    standard string format: 'YYYY-MM-DD HH:MM:SS'.

    Supported Formats:
    1. ISO 8601 with 'T' and 'Z' -> e.g., "2026-07-01T15:30:00Z"
    2. Slashes with space     -> e.g., "2026/07/01 15:30:00"
    3. Hyphens with space     -> e.g., "2026-07-01 15:30:00"

    Requirements:
    - If a string does not match any of the 3 formats above, print "Invalid date format",
      skip that specific record, and continue processing the rest.
    - Do not let the function crash on corrupted or unexpected strings.

    Args:
        raw_dates (list of str): A list containing date strings in different formats,
                                 potentially including corrupt or invalid data.

    Returns:
        list of str: A list of successfully standardized date strings in
                     'YYYY-MM-DD HH:MM:SS' format.

    Example Input:
        raw_dates = [
            "2026-07-01T10:15:30Z",
            "2026/07/01 11:20:00",
            "invalid-date-string",
            "2026-07-01 12:05:00"
        ]

    Example Output:
        [
            "2026-07-01 10:15:30",
            "2026-07-01 11:20:00",
            "2026-07-01 12:05:00"
        ]
    """
    pass

    """ 모범답안
    1. 입력 받는 허용 포맷 리스트를 만든다.
    2. try-except 문 안에서 strptime() 으로 datetime obj를 파싱한다.
    3. 만약 해당 포맷이 아니라면 exception이 나오고 pass 해서 다음 포맷을 대입해본다.
    4. 만약 해당 포맷이 맞다면 새 리스트에 strftime()으로 스트링으로 넣어준다. 
    5. flag 로 다음 룹에 들어가지 않도록 막아준다. 
    6. 아무 포맷과도 매칭되지 않으면 실패 로그를 남긴다. 
    7. 결과 리스트를 리턴한다.

    formats = ["%Y-%m-%dT%H:%M:%S", "%Y/%m/%d %H:%M:%S", "%Y-%m-%d %H:%M:%S"]
    new_dates = []
    for date_str in raw_dates:
        # 문자열 처리: 타임존 Z를 문자열에서 빼버림
        date_str = date_str.replace("Z", "")
        matching_format = False
        for fmt in formats:
            try:
                # 만약 이 포맷과 안맞으면 에러 뱉음
                date_obj = datetime.strptime(date_str, fmt)
                new_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
                new_dates.append(new_date)
                matching_format = True
                break
            except ValueError:
                pass
        if not matching_format:
            print('No matching format')
    print(new_dates)
    return new_dates 
    """
raw_dates = [
    "2026-07-01T10:15:30Z",
    "2026/07/01 11:20:00",
    "invalid-date-string",
    "2026-07-01 12:05:00",
]
standardize_dates(raw_dates)
