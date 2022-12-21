//프로그래머스 level 0
//https://school.programmers.co.kr/learn/courses/30/lessons/120891#

function solution(order) {
    let count = 0;
    order.toString().split("").map((c)=>{
        if (c==3 || c==6 || c==9) count++;
    });
    return count;
}
