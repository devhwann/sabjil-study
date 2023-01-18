function solution(num_list, n) {
    // 풀이 못해서 다른 사람의 풀이를 참고한 답안입니다 : ) 
    const answer = [];
    while(num_list.length !== 0) {
        answer.push(num_list.splice(0, n));   
    }
    return answer;
}