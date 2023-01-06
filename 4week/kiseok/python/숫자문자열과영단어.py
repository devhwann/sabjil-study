# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    numli=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(numli)):
        s = s.replace(numli[i], str(i))

    return int(s)