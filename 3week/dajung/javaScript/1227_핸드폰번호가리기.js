//프로그래머스 level 1
//https://school.programmers.co.kr/learn/courses/30/lessons/12948?language=javascript#

//문자열 phone_number
function solution(phone_number) {
    return phone_number.split("").reduce((sum, num, idx) => {
        if(idx < phone_number.length - 4)
            return sum += "*";
        else return sum += num;
    }, "")
}
