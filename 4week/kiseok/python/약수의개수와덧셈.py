# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def find_num(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    # print(n,cnt)
    return cnt

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if find_num(i)%2==0:
            answer+=i
        else:
            answer-=i
    return answer