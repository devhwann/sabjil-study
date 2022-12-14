#https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    answer = ''.join([i*n for i in my_string])
    return answer