def solution(num):
    cnt = 0

    while num != 1:
        cnt += 1

        if cnt > 500:
            return -1
        elif num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1

    return cnt
