#https://school.programmers.co.kr/learn/courses/30/lessons/120811

def solution(array):
    array.sort()
    answer = array[len(array)//2]
    return answer