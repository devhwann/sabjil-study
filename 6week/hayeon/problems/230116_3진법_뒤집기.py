def solution(n):
    three = ""

    while n:
        three += str(n % 3)
        n //= 3

    return int(three, 3)
