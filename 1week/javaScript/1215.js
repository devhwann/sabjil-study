// 삼각형의 완성조건(1)
// https://school.programmers.co.kr/learn/courses/30/lessons/120889
function solution(sides) {
    sides.sort(function(a, b){
       return b - a
    });
    if(sides[0] >= sides[1]+sides[2]){
        return 2;
    } else {
        return 1;
    }
}
