# https://school.programmers.co.kr/learn/courses/30/lessons/120840

def solution(balls, share):
    u,l=1,1
    for i in range(share+1,balls+1):
        u*=i
    for i in range(1,balls-share+1):
        l*=i
    answer = u/l
    return answer