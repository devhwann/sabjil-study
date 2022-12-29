# https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    n_min_li=[i for i in range(n,0,-1) if n%i==0]
    m_min_li=[i for i in range(1,m+1) if m%i==0]
    for i in n_min_li:
        if i!=0 and i in m_min_li:
            answer.append(i)
            break
    answer.append(n*m/answer[0])
    return answer