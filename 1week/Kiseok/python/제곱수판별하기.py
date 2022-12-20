#https://school.programmers.co.kr/learn/courses/30/lessons/120909

import math
def solution(n):
    answer = 1 if math.sqrt(n)%1==0 else 2
    return answer