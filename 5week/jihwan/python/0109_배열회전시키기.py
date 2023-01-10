# 프로그래머스 Level 0 0109_배열회전시키기
# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(numbers, direction):
    answer = []
    
    if(direction == 'right'):              
            answer.append(numbers[-1])
            answer += numbers[0:-1]
    if(direction == 'left'):
            answer += numbers[1:]
            answer.append(numbers[0])
                           
    return answer
