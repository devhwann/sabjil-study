//프로그래머스 level 2
//https://school.programmers.co.kr/learn/courses/30/lessons/12951

//문자열 s
//공백이 연속적으로 나올 때 주의
function solution(s) {
    return s.toLowerCase().split(" ").map((str) => {
        return str.charAt(0).toUpperCase() + str.slice(1)
    }).join(" ")
}

