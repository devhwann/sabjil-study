#https://school.programmers.co.kr/learn/courses/30/lessons/120908

def solution(str1, str2):
    for i in range(len(str1)-len(str2)+1):
        if "".join(str1[i:i+len(str2)])==str2:
            return 1
    return 2