def solution(n):
    i = 2
    answer = set()

    while n > 1:
        if n % i == 0:
            answer.add(i)
            n //= i
        else:
            i += 1

    return answer


print(solution(12))
