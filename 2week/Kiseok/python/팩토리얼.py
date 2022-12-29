# https://school.programmers.co.kr/learn/courses/30/lessons/120848

def solution(n):
    tmp=1
    for i in range(1,11):
        tmp*=i
        if tmp>n:
            return i-1
    return 10