#https://school.programmers.co.kr/learn/courses/30/lessons/120889

def solution(sides):
    answer = 2-(sum(sides)>2*max(sides))
    return answer