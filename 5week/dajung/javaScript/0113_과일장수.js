//프로그래머스 level 1
//https://school.programmers.co.kr/learn/courses/30/lessons/135808?language=javascript#

//k : 사과의 최대 상태점수, m : 박스당 사과 개수, p*m : 한 상자의 가격
//최대이익, 상자 단위 판매, 남는 사과 폐기
function solution(k, m, score) {
    let sum = 0;
    score.sort((a, b)=> b-a);

    for (let i=m-1; i<score.length; i+=m) {
        sum += score[i]*m;
    }
    return sum
}
