def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for i, num in enumerate(answers):
        if num == a[i % 5]:
            score[0] += 1
        if num == b[i % 8]:
            score[1] += 1
        if num == c[i % 10]:
            score[2] += 1

    return [i + 1 for i, s in enumerate(score) if s == max(score)]
