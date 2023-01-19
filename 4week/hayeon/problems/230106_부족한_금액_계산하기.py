def solution(price, money, count):
    answer = money - sum([price * c for c in range(count + 1)])

    return abs(answer) if answer < 0 else 0
