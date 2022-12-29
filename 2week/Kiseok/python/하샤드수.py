# https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = x%sum(list(map(int,str(x))))==0
    return answer