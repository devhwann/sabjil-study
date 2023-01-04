//프로그래머스 level 2
//https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=javascript

//먼저 배포돼야 하는 순서대로 작업 진도가 적힌 정수 배열 progresses (작업의 개수는 100개 이하)
//각 작업의 개발 속도가 적힌 정수 배열 speeds
//배포는 하루의 끝에 한 번, 
//각 배포마다 몇 개의 기능이 배포되는지 return 
function solution(progresses, speeds) {
    //앞 순서부터 나와야 하니 큐 사용
    let queue = [];

    for (let i=0; i<100; i++) {
        for(let j=0; j<progresses.length; j++) {
            progresses[j] += speeds[j]; //작업 수행
        }
        let count = 0; //앞에서부터 100 달성한 작업 개수, 가장 바깥 반복문이 돌 때마다 0으로 초기화
        while(1) {
            if(progresses[count] >= 100) 
                count++; 
            else{
                if (count !== 0){ //100넘은 작업이 1개도 없을 때 0을 큐에 넣는 것 방지
                    queue.push(count); //배포할 작업 개수 큐에 넣기
                    progresses.splice(0, count); //큐에 넣은 작업 개수만큼 삭제
                    speeds.splice(0, count); 
                }
                break; //앞에서부터 100넘은 작업 확인하다가 100미만인 작업 발견하면 break
            }
        }  
        if(progresses.length === 0) break; //더이상 처리할 작업이 없으면 반복 중지
    }
    return queue;
}