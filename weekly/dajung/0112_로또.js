//프로그래머스 level
//https://school.programmers.co.kr/learn/courses/30/lessons/77484#

//로또 번호 배열 lottos, 당첨 번호 배열 win_nums
//당첨 가능한 최고 순위와 최저 순위
function solution(lottos, win_nums) {
    let max = 0;
    let min = 0;
    let zero = 0;
    let dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6};
    lottos.map((n)=>{
        if(n === 0) zero++; 
        if (win_nums.includes(n))
            min++;
    })
    max = min + zero;
    
    return [dic[max], dic[min]]
}