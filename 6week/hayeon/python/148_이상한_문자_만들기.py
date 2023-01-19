def solution(s):
    str = list()
    word = s.split(" ")

    for w in word:
        trans = ""

        for i, c in enumerate(w):
            trans += c.upper() if i % 2 == 0 else c.lower()

        str.append(trans)

    return " ".join(str)
