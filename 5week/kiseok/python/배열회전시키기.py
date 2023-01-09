# https://school.programmers.co.kr/learn/courses/30/lessons/120844

def solution(numbers, direction):
    answer = []
    if direction == 'left':
        return numbers[1:]+[numbers[0]]
    else:
        return [numbers[-1]]+numbers[:-1]