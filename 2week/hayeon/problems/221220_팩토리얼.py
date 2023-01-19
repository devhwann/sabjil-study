def solution(n):
    factorial = 1
    i = 1

    while True:
        factorial *= i

        if n < factorial:
            return i - 1

        i += 1
