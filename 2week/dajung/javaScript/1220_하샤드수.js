//프로그래머스 level 1
//https://school.programmers.co.kr/learn/courses/30/lessons/12947#
//1 <= x <= 10000

function solution(x) {
    //숫자를 문자열로 변환, split으로 배열로 변환 후 각 자릿수 더함
    let sum = x.toString().split("").reduce((sum, cur)=>sum += parseInt(cur),0);
    if (x%sum === 0) return true;
    else return false;
}
