#https://school.programmers.co.kr/learn/courses/30/lessons/120822

def solution(my_string):
    answer = ''
    for i in my_string:
        answer=i+answer
    return answer