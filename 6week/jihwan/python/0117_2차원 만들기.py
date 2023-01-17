# 프로그래머스 level 0 0117_2차원 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120842?language=python3
def solution(num_list, n):
    answer = []
    # Start, Stop, Step  
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n]) 
        print(answer)
        print(i)
    return answer