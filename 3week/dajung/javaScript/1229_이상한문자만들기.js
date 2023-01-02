//프로그래머스 level 1
//https://school.programmers.co.kr/learn/courses/30/lessons/12930#

//문자열 s
function solution(s) {
    //문자열->단어별 배열
    return s.split(" ").map((str) => {
        let tmp = "";
        for (let i = 0; i<str.length; i++){
            if(i%2 === 0) tmp += str.charAt(i).toUpperCase();
            else tmp += str.charAt(i).toLowerCase();
        }
        return tmp
    }).join(" ");
}
