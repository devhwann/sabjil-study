def solution(s):
    s = s.lower()
    answer = []

    for i in s.split(" "):
        if len(i) > 0 and i[0].isalpha():
            i = i[0].upper() + i[1:]

        answer.append(i)

    return " ".join(answer)
