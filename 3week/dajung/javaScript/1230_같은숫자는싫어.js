//프로그래머스 level 1
//https://school.programmers.co.kr/learn/courses/30/lessons/12906#

//배열 arr (0 <= 원소 크기 <= 9)
//연속적인 숫자 제거
function solution(arr)
{
    let queue = [];
    //중복 없는 큐
    arr.map((n, idx)=>{
        if(arr[idx-1] !== n) queue.push(n);
    })
    return queue
}

