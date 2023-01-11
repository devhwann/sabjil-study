#프로그래머스 level 0
#https://school.programmers.co.kr/learn/courses/30/lessons/120844?language=python3

# def solution(numbers, direction):
#     tmp = [0]*len(numbers)
#     if direction == "right":
#         tmp[0] = numbers[len(numbers)-1]
#         for i in range(len(numbers)-1):
#             tmp[i+1] = numbers[i]
#     else:
#         for j in range(len(numbers)-1):
#             tmp[j] = numbers[j+1]
#         tmp[len(numbers)-1] = numbers[0]
#     return tmp

from collections import deque
def solution(numbers, direction):
    tmp = deque(numbers)
    tmp.rotate(1) if direction == "right" else tmp.rotate(-1)
    return list(tmp)

#deque 활용
