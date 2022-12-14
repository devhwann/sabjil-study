// 1214 양꼬치
// https://school.programmers.co.kr/learn/courses/30/lessons/120830
function solution(n, k) {
    var answer = 0;
    if(n>=10){
        var service = Math.floor(n / 10);
        answer = 12000*n+2000*(k-service);    
    } else {
        answer = 12000*n+2000*k;
    }
    return answer;
}