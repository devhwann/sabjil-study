#https://school.programmers.co.kr/learn/courses/30/lessons/120837

def solution(hp):
    answer = hp//5 + hp%5//3 +hp%5%3
    return answer