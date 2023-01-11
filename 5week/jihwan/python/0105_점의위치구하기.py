# //프로그래머스 level 0
# //https://school.programmers.co.kr/learn/courses/30/lessons/120841#

def solution(dot):
  
        if(dot[0] > 0 and dot[1] > 0) :
            return 1
        elif(dot[0] < 0 and dot[1] > 0) :
            return 2
        elif(dot[0] > 0 and dot[1] < 0) :
            return 4         
        elif(dot[0] < 0 and dot[1] < 0) :
            return 3
               
        