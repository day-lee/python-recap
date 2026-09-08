# https://www.freecodecamp.org/learn/daily-coding-challenge/11-04
- case-sensitive하므로 클렌징이 필요하다.
- 비교를 위해서는 IN operator 사용 가능하다.

def image_search(images, term):
    # r = []
    # for word in images:
    #     if term.lower() in word.lower() :
    #         r.append(word)
    # print(r)
    r = [word for word in images if term.lower() in word.lower() ]
    print(r)
    return r

image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog")
image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG")
image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat")
