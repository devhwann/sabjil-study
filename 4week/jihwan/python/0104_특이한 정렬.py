# 프로그래머스 Level 0 0104_특이한 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/120880?language=python3
def solution(numlist, n) :
    answer = []
        
    for i in range (len(numlist)) :
        if(n == numlist[i]) :
            answer.append(n)
            
    for i in range(1,10000): # 1 ≤ n ≤ 10,000 1 ≤ numlist의 원소 ≤ 10,000             
        if n  + i in numlist:  # n보다 큰 수 순회
            answer.append(n + i)            
        if n - i in numlist: # 4-1 = 3 ?  n보다 작은 수 순회 
            answer.append(n -i)  
     
       
    return answer
