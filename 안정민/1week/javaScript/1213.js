// 짝수 홀수 개수
// https://school.programmers.co.kr/learn/courses/30/lessons/120824#

function solution(num_list) {
    var answer = [];
    var jjak = 0;
    var hol = 0;
    for(i of num_list){
        if(i % 2 == 0){
            jjak += 1
        } else {
            hol += 1
        }
    }
    answer.push(jjak);
    answer.push(hol);
    return answer;
}