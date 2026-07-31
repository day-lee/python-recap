# https://www.freecodecamp.org/learn/daily-coding-challenge/07-31

def decode_morse(code):
# - create a key:value pair of morse code 
#  code = {'.-': 'A' ..}

# - string into list with separator empty space. split(" ")

# - loop over and match with dict.get 
#     append in a list 
# - return list into str with empty space 

# - exceptions.. what if there is no matching key? early return 
# - space between words is 2 empty spaces, so clean it before splitting.

    morse_code = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
        '--..': 'Z'
    }
    # 스트링 양옆 공백 클렌징 .strip(), 단어 단위 분리

    words = code.strip().split("   ")
    result = []
    for word in words:
        letters = word.split(" ")
        for char in letters:
            alphabet = morse_code.get(char, "?")
            if alphabet != '?':
                result.append(alphabet)
        result.append(" ")  # Add space between words
    print("".join(result))

decode_morse("... --- ... 3") # SOS
decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -..") # "HELLO WORLD"