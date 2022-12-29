# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    #index쓰지말기
    tmp = []
    for i in range(len(emergency)):
        tmp.append([emergency[i],i])
    tmp.sort()
    
    answer=[]
    for i,j in tmp:
        answer.append(len(emergency)-j)
        
    return answer