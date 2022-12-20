#https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    vowel=['a','e','i','o','u']
    answer=''
    for i in my_string:
        if i not in vowel:
            answer+=i
    return answer