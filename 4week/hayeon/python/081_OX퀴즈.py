def solution(quiz):
    answer = []

    for q in quiz:
        q = q.replace("=", "==")

        if eval(q) == True:
            answer.append("O")
        else:
            answer.append("X")

    return answer
