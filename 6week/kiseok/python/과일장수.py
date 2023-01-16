# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(1,len(score)//m+1):
        answer+=score[i*m-1]*m

    return answer