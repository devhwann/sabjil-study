#https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    answer = ''
    for i in rsp:
        answer+= '0' if i=="2" else '2' if i=="5" else '5'
    return answer