#프로그래머스 level 0
#https://school.programmers.co.kr/learn/courses/30/lessons/120840?language=python3#

#서로 다른 구슬 balls개 중 share개의 구슬 고르기

# def calcul(bigger, total):
#     result = 1
#     for i in range(bigger+1, total+1):
#         result *= i
#         result /= (total-i+1)
#     return int(result)

# def solution(balls, share):
#     if balls - share <= share:
#         return calcul(share, balls)
#     else:
#         return calcul(balls-share, balls)


#DP
def dynamic(n):
    result = {}
    if n == 0 or n == 1: 
        result[n] = 1
        return 1
    elif n in result:
        return result[n]
    else:
        fac = n * dynamic(n-1)
        result[n] = fac
        return fac

def solution(balls, share):
    return dynamic(balls) // (dynamic(balls-share) * dynamic(share))

