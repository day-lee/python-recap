- emoji는 내부적으로 문자열 유니코드이다. type('⭐') 해보면 str 나온다.
- 파이썬 딕셔너리를 불변 객체를 immutable을 키로 사용할 수 있다: "str, int, float, tuple, bool"
- mutable은 "list, dict, set"는 키로 사용 불가
- 상수 Constant는 PEP8에 따라 대문자로 작성하기 EMOJI_DICT

EMOJI_DICT = {
'👶': "baby",
'🐱': "cat",
'🐕': "dog",
'🐟': 'fish',
'🥵': 'hot',
'🧊': 'ice',
'🪨': 'rock',
'🦈': 'shark',
'🍲': 'soup',
'⭐': "star"
}

# use + to concatenate string and empty space to separate words.
def get_emoji_phrase(s):
    result = ""
    for emoji in s:
        result += EMOJI_DICT[emoji] + " "
        # result += " "
    return result.strip()


# refactored by AI
# list comprehension is shorter, use less variable memory space, quicker as it's more optimised under the hood.
def get_emoji_phrase_2(s):
    word = [EMOJI_DICT.get(emoji) for emoji in s ]
    return " ".join(word)


print(get_emoji_phrase("🪨⭐")) #rock star
print(get_emoji_phrase("🧊🧊👶")) #ice ice baby

print(get_emoji_phrase_2("🪨⭐")) #rock star
print(get_emoji_phrase_2("🧊🧊👶")) #ice ice baby