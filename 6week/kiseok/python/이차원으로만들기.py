# https://school.programmers.co.kr/learn/courses/30/lessons/120842

def solution(num_list, n):
    answer = [num_list[i:i+n] for i in range(0,len(num_list),n)]
    return answer