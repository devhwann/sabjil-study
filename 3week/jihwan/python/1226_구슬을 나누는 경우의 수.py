# 0 구술을 나누는 경우의 수
# https://school.programmers.co.kr/learn/courses/30/lessons/120840?language=python3

def solution(balls, share):    
    return factorial(balls) / (factorial(balls - share) * factorial(share))

# 팩토리얼 구하는 함수
def factorial(n):
    result = 1
    for i in range(2, n +1) :
        result = result * i       
    return result