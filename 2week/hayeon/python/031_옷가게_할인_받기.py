def solution(price):
    return int(
        price
        * {price >= 100000: 0.95, price >= 300000: 0.90, price >= 500000: 0.80}.get(
            True, 1
        )
    )
