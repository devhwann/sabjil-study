def solution(spell, dic):
    for d in dic:
        if set(list(d)) == set(spell):
            return 1
    else:
        return 2
