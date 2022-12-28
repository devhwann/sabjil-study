#프로그래머스 level 0
#https://school.programmers.co.kr/learn/courses/30/lessons/120834?language=python3#

#age는 자연수, 행성은 알파벳 소문자만 사용
def solution(age):
    ageDic = {}
    result = ""
    idx = 0
    #나이 변환 딕셔너리 세팅
    for i in range(0,10):
        ageDic[i] = chr(i + 97)
    strage = str(age)
    while(1):
        if idx >= len(strage):
            break
        result += ageDic[int(strage[idx])]
        idx += 1
    return result
