//프로그래머스 level 1
//https://school.programmers.co.kr/learn/courses/30/lessons/12940#

function solution(n, m) {
    let arr = [];
    let result = [];
    //최대공약수
    for(let i=1; i<=m; i++){
        if(n%i === 0 && m%i === 0)
            arr.push(i);
    }
    result.push(arr[arr.length-1]);//약수 중 최대 수 삽입
    //최소공배수
    let num = 1;
    while(1){//루프 횟수 모르므로 while 사용
        if(num%n === 0 && num%m === 0)//num증가시키며 n과 m으로 나눌 수 있는 최소 수 찾기
            break;
        num++;
    }
    result.push(num);
    return result;
}