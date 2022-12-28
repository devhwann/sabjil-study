# 프로그래머스 Level 0 1228_외계행성의나이
# https://school.programmers.co.kr/learn/courses/30/lessons/120834?language=python3

def solution(age):
   
    alphabet = []
    result = ''
    for i in range(97,107) : # 아스키 코드 a ~ j
        alphabet.append(chr(i)) 
    
    for i in str(age):
        result += alphabet[int(i)]        
                                
    return result