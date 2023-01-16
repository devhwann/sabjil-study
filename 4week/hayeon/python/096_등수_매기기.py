def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)

    return [rank.index(sum(s) / 2) + 1 for s in score]
