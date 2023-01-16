def solution(n):
    result = ''

    while n >= 1:
        rest = n % 3
        n = n // 3
        result += str(rest)
    # int(string, base) : n진수 -> 10진수    
    return int(result, 3)