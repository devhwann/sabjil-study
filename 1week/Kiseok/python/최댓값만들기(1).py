#https://school.programmers.co.kr/learn/courses/30/lessons/120847

def solution(numbers):
    numbers.sort()
    answer = numbers[-1]*numbers[-2]
    return answer