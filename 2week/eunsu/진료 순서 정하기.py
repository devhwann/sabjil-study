# 프로그래머스

def solution(emergency):
    answer = [1] * len(emergency)
    for i in range(0, len(emergency)):
        for j in range(0, len(emergency)):
            if emergency[i] < emergency[j]:
                answer[i] += 1
    return answer