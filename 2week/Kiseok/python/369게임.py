# https://school.programmers.co.kr/learn/courses/30/lessons/120891

def solution(order):
    answer = sum([1 if int(i) in (3,6,9) else 0 for i in str(order) ])
    return answer