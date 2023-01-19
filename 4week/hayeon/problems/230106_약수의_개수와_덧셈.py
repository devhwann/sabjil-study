def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        square = i ** (1 / 2)

        if int(square) == square:
            answer -= i
        else:
            answer += i

    return answer
