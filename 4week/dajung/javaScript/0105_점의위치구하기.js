//프로그래머스 level 0
//https://school.programmers.co.kr/learn/courses/30/lessons/120841#

//정수 배열 dot
function solution(dot) {
    if (dot[0] > 0){
        if(dot[1] > 0)
            return 1
        return 4
    } else {
        if (dot[1] > 0)
            return 2
        return 3
    }
}

