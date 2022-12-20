//프로그래머스 level 0
//https://school.programmers.co.kr/learn/courses/30/lessons/120835
//입력값 정수배열
//루프 한번마다 compare 변수를 설정해서 순위값 부여

function solution(emergency) {
    //응급도가 클수록 먼저 진료
    let compare = 0;
    let result = [];
    for (let i=0; i<emergency.length; i++){
        let sequence = 1; //처음 순위 1로 시작
        compare = emergency[i];
        for (let j=0; j<emergency.length; j++){
            //comare변수보다 우선순위가 큰 수를 발견할때마다 순위 하락
            if(compare<emergency[j]) sequence++;
        }
        result.push(sequence); //결과 배열에 순서대로 입력
    }
    return result;
}
