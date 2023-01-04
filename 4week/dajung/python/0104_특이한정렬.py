#프로그래머스 level 0
#https://school.programmers.co.kr/learn/courses/30/lessons/120880

#정수가 담긴 배열 numlist(중복 x), 정수 n
#절대값이 더 작을 수록 배열의 앞으로 온다. 같은 거리를 가질 경우 큰 값이 앞으로 온다.

def solution(numlist, n):
    #sorted함수의 정렬 기준 지정(key 옵션에 함수 지정하면 각 원소에 이 함수를 호출한 결과를 기준으로 대소비교)
    #lambda 매개변수 : 표현식
    #abs(num-n) 기준으로 정렬하나 같은 값이 나온다면 -num을 오름차순으로 정렬하는 방식
    return sorted(numlist, key = lambda num: (abs(num-n), -num))



