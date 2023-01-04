# https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math
def solution(progresses, speeds):
    answer = []
    tmp_p=[]
    for i in range(len(progresses)):
        tmp_p.append(math.ceil((100-progresses[i])/speeds[i]))
    
    cnt,old=0,tmp_p[0]
    for i in tmp_p[1:]:
        cnt+=1
        if old<i:
            answer.append(cnt)
            cnt,old=0,i
    answer.append(cnt+1)
    return answer