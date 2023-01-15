def solution(num, total):
    start = total // num - (num // 2 - 1) if num % 2 == 0 else total // num - (num // 2)

    return list(range(start, start + num))
