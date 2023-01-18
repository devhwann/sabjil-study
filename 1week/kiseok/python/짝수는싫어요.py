#https://school.programmers.co.kr/learn/courses/30/lessons/120813?language=python3

def solution(n):
    answer = [i for i in range(n+1) if i%2==1]
    return answer