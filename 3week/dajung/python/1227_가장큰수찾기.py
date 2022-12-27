#프로그래머스 level 0
#https://school.programmers.co.kr/learn/courses/30/lessons/120899?language=python3

def solution(array):
    return [max(array), array.index(max(array))]