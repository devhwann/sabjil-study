# https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    alphabet='abcdefghij'
    answer = ""
    for i in str(age):
        answer+=alphabet[int(i)]
    return answer