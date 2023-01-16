# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    transformed_n=""
    while n:
        n,s=divmod(n,3)
        transformed_n+=str(s)
    return int(transformed_n,3)