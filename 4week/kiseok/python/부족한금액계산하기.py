# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    if price*sum(list(range(1,count+1)))>money:
        return price*sum(list(range(1,count+1)))-money
    return 0