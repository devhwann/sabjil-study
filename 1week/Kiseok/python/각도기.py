#https://school.programmers.co.kr/learn/courses/30/lessons/120829

def solution(angle):
    answer = 1 if angle<90 else 2 if angle==90 else 3 if angle>90 and angle<180 else 4
    return answer