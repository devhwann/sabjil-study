import math


def solution(progresses, speeds):
    answer = []
    front = 0

    time = [
        math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))
    ]

    for i in range(len(time)):
        if time[i] > time[front]:
            answer.append(i - front)
            front = i

    answer.append(len(time) - front)

    return answer
