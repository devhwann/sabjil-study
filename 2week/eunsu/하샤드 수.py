# 프로그래머스

def solution(x):
    answer = True

    x_list = list(str(x))
    x_sum = 0

    for i in x_list:
        x_sum += int(i)

    if x % x_sum == 0:
        return answer
    else:
        return False