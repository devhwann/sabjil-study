#https://school.programmers.co.kr/learn/courses/30/lessons/120830

def solution(n, k):
    answer = 12000*n+2000*(k-n//10)
    return answer