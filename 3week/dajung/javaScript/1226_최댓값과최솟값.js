//프로그래머스 level 2
//https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=javascript

//문자열 s
function solution(s) {
    let arr = s.split(" ").map(c => parseInt(c))
    let str = [Math.min(...arr), Math.max(...arr)]
    return str.join(" ")
}

//Math.max()는 내부적으로 최대값을 찾기 전에 Number로 변환하려고 시도하므로 문자열을 숫자로 변환할 필요가 없다.
//문자열 중 하나라도 숫자가 아니라면 return NaN 