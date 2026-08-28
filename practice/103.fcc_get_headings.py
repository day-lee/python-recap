# https://www.freecodecamp.org/learn/daily-coding-challenge/09-28

def get_headings(csv):
    if not csv:
        return [] # defensive coding, early return
    r = [letter.strip() for letter in csv.split(",")]
    print(r)
    return r

get_headings("name,age,city") # ["name", "age", "city"]
get_headings("username , email , signup date ") # ['username', 'email', 'signup date']