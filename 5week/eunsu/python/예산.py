def solution(d, budget):    
    result = 0
    # 많은 부서를 지원 -> 신청금액이 적은 부서부터 지원
    d.sort()
    
    for i in range(len(d)): 
        if d[i] <= budget:
            result += 1    
            budget -= d[i]  
            
    return result