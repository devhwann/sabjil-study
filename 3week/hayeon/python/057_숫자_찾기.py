def solution(num, k):
    for i, c in enumerate(str(num)):
        if c == str(k):
            return i + 1
    return -1
