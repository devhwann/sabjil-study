//프로그래머스 level 1
//https://school.programmers.co.kr/learn/courses/30/lessons/12932

function solution(n) {
    return n.toString().split("").reverse().map(i=>parseInt(i));
}
