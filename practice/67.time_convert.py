def TimeConvert(num:int)-> str:
  """
  =============================================================================
  [INSTRUCTIONS & CHALLENGE DESCRIPTION]
  =============================================================================
  Have the function TimeConvert(num) take the num parameter being passed 
  and return the number of hours and minutes the parameter converts to 
  (ie. if num = 63 then the output should be 1:3). 
  
  Separate the number of hours and minutes with a colon.

  =============================================================================
  [EXAMPLES]
  =============================================================================
  Input: 126
  Output: "2:6"

  Input: 45
  Output: "0:45"
  """



pass 










""" 모범 답안: 분을 두자리로 맞출 때 f string formatting
  # divmod()는 몫과 나머지를 동시에 구하는 빌트인 함수 // 몫, %나머지
  hours, minutes = divmod(num, 60)
  
  #fstring ":0" 빈자리 0으로 채우기, "2" 두자리 확보, "d" 데이터는 10진수 decimal 정수 
  return f"{hours}:{minutes:02d}"  
"""  

#   hour = num // 60 
#   minutes = num % 60 
#   if len(str(minutes)) == 1:
#     minutes = f"0{minutes}"
#   return f"{hour}:{minutes}"

# --- Test Cases to Verify Your Logic ---
print(TimeConvert(126))  # Should print: "2:6"
print(TimeConvert(45))   # Should print: "0:45"
print(TimeConvert(63))   # Should print: "1:3"
