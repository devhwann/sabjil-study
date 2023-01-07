//프로그래머스 level 1
//https://school.programmers.co.kr/learn/courses/30/lessons/77884?language=javascript#

function solution(left, right) {
    let odd = []; //홀수
    let even = []; //짝수
    
    for (let i=left; i<=right; i++) {
        let count = 0;
        for(let j=1; j<=i; j++){
            if(i%j == 0) {
                count++;
            }
        }
        if(count%2 == 0) even.push(i);
        else odd.push(i);
    }
    return even.reduce((sum, n)=> sum += n) - odd.reduce((sum, n)=> sum += n);
}