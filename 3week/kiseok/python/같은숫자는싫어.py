#https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer=[arr[0]]
    cnt=0
    for i in arr[1:]:
        new=i
        old=answer[cnt]
        if old!=new:
            answer.append(new)
            cnt+=1
    return answer