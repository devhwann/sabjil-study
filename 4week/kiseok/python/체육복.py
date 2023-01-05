# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    del_li=[]
    for i in reserve:
        if i in lost:
            del_li.append(i)
    for i in del_li:
        reserve.pop(reserve.index(i))
        lost.pop(lost.index(i))

    while len(lost)>0 and len(reserve)>0:
        r=reserve.pop(0)
        for i in lost:
            if i in range(r-1,r+2):
                lost.pop(lost.index(i))
                break
        
    answer = n-len(lost)
    return answer