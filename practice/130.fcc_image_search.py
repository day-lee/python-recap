# https://www.freecodecamp.org/learn/daily-coding-challenge/11-04
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
