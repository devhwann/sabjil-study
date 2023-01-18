def solution(n, lost, reserve):
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)

    for i in _lost:
        if i - 1 in _reserve:
            _reserve.remove(i - 1)
        elif i + 1 in _reserve:
            _reserve.remove(i + 1)
        else:
            n -= 1

    return n
