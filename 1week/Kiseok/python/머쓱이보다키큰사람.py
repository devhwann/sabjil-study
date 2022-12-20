#https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    answer = 0
    for i in array:
        if i>height:
            answer+=1

    return answer