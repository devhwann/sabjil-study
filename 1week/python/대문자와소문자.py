#https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    answer = ''
    for s in my_string:
        if s.isupper():
            answer+=s.lower()
        else:
            answer+=s.upper()

    return answer