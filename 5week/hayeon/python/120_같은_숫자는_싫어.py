def solution(arr):
    answer = list()

    for a in arr:
        if answer[-1:] == [a]:
            continue
        else:
            answer.append(a)

    return answer
