def solution(participant, completion):
    part = dict()

    for p in participant:
        if part.get(p) == None:
            part[p] = 1
        else:
            part[p] += 1

    for c in completion:
        part[c] -= 1

    for key, value in part.items():
        if value != 0:
            return key
