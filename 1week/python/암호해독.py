#https://school.programmers.co.kr/learn/courses/30/lessons/120892

def solution(cipher, code):
    answer = ""
    for i in range(len(cipher)//code):
        answer+=cipher[code-1+code*i]
    
    return answer