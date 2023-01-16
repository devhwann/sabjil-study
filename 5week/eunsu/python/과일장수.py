def solution(k, m, score):
    result = 0
    score.sort(reverse = True)
    
    for i in range(0, len(score), m):
        box = score[i:i+m]
        
        if len(box) == m:
            result += min(box) * m
        
    return result