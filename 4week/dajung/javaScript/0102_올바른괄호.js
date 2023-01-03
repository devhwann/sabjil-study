//프로그래머스 level 2
//https://school.programmers.co.kr/learn/courses/30/lessons/12909

//길이 100,000 이하의 문자열 s
function solution(s){
    let stack = [];
    let splited = s.split("");

    for(let i=0; i<splited.length; i++){
        //맨 처음 값으로 )이 들어오거나 문자열의 길이가 1일 경우
        if(splited.length === 1 || splited[0] === ")") return false;
        else {
            //(뒤에 )가 들어오는 경우
            if(splited[i] === ")" && stack.at(-1) === "(") stack.pop();
            else stack.push(splited[i]);
        }
    }
    if (stack.length !== 0)
        return false;
    return true;
}
