// 삼각형의 완성조건(2)
//https://school.programmers.co.kr/learn/courses/30/lessons/120868
function solution(sides) {
    sides.sort(function(a, b){
        return a-b
    })
    // 둘 중 하나가 가장 긴 변일 때..
    var a = sides[1] - sides[0]
    var b = sides[1] - a
    // 나머지 한변이 가장 긴 변일 때..
    var c = sides[0] + sides[1] - 1 - sides[1]
    return b + c
}