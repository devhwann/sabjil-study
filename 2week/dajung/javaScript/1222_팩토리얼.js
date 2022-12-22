//프로그래머스 level 0
//https://school.programmers.co.kr/learn/courses/30/lessons/120848

//클로저 방식
// function closure(n, num, arg){
//     return function factorial(n, num, arg){
//         if (n<num) {
//             console.log(num, arg);
//             return arg-1;
//         }
//         factorial(num*(arg+1), arg+1);
//     }
// }

function factorial(n, num, arg) {
    if (n<num) {
        return arg-1;
    }
    console.log(arg);
    factorial(n, num*(arg+1), arg+1);
}

console.log(factorial(7, 1,1));

function solution(n) {
    // let fac = new closure();
    // let num = n;
    // return fac(num, 1, 1);
    return factorial(n, 1, 1);
}

console.log(solution(7));//undefined 출력됨... 왜인지 아직 모르겠음, 원인 분석 후 수정할 예정


