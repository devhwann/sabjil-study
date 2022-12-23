//프로그래머스 level 1
//https://school.programmers.co.kr/learn/courses/30/lessons/12916

//문자열 s 입력
//대소문자 구별 x
function solution(s){
    //reduce함수로 객체 반환
    let object = s.toLowerCase().split("").reduce((obj, char)=>{
        if(char === 'p') obj['p']++;
        else if(char === 'y') obj['y']++; 
        return obj;
    }, {p:0, y:0})
    return object.p === object.y ? true : false;
}
