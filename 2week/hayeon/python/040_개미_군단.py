def solution(hp):
    count = 0

    for i in [5, 3, 1]:
        count += hp // i
        hp %= i

    return count
