def solution(s):
    return "".join(sorted([c for c in set(s) if s.count(c) == 1]))
