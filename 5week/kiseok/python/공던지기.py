# https://school.programmers.co.kr/learn/courses/30/lessons/120843?language=python3

def solution(numbers, k):
    while len(numbers)<=k*2:
        numbers+=numbers
    return numbers[(k-1)*2]