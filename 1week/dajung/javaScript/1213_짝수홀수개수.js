function solution(num_list) {
    var answer = [];
    let even = [];
    let odd = [];
    for (let i=0; i<num_list.length; i++){
        if (num_list[i]%2 === 0){//짝수일 때
            even.push(num_list[i]);
        } else {//홀수일 때
            odd.push(num_list[i]);
        }
    }
    answer.push(even.length);
    answer.push(odd.length);
    return answer;
}