// 제곱수 판별하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120909
function solution(n) {
    var i = Math.sqrt(n);
    if (n % i == 0) return 1;
    else return 2;
}