def solution(lottos, win_nums):
    hit = len(set(lottos) & set(win_nums))
    rank = [6, 6, 5, 4, 3, 2, 1]

    return [rank[(hit + lottos.count(0)) % 7], rank[hit]]
