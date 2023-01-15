def solution(s):
    for i, n in enumerate(s := s.split(" ")):
        if n == "Z":
            s[i] = -s[i - 1]
        else:
            s[i] = int(n)

    return sum(s)
