# https://school.programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    idx=0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = "김서방은 "+str(i)+"에 있다"
            return answer
    