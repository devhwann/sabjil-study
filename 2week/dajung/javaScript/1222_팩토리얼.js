//프로그래머스 level 0
//https://school.programmers.co.kr/learn/courses/30/lessons/120848
//오류 해결...재귀함수 사용

function factorial(n, num, arg) {
    if (n<num) {
        return arg-1;
    }
    return factorial(n, num*(arg+1), arg+1);
}
function solution(n) {
    return factorial(n, 1, 1);
}
