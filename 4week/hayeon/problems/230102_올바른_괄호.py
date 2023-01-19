from collections import deque


def solution(s):
    d = deque()

    for i in s:
        if i == "(":
            d.append(i)
        elif i == ")" and d:
            d.pop()
        elif i == ")" and not d:
            d.append(")")

    return False if d else True
