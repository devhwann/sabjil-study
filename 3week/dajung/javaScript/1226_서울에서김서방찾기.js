//프로그래머스 level 1
//https://school.programmers.co.kr/learn/courses/30/lessons/12919

//String 배열 seoul
function solution(seoul) {
    let index = seoul.map((str, idx) => {
        if (str === "Kim") return idx
    }).join("")
    return `김서방은 ${index}에 있다`
}
