#  프로그래머스 Level 0 1215_삼각형의 완성조건(1)
#  https://school.programmers.co.kr/learn/courses/30/lessons/120889?language=javascript

def solution(sides):
    sides.sort()    
    return 1 if sides[0] + sides[1] > sides[2] else 2
  
  
  #  max 를 이용한 풀이 신기.. max(sides) < .. 
