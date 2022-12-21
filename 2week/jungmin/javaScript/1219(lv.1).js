// 부족한 금액 계산하기
// https://school.programmers.co.kr/learn/courses/30/lessons/82612
function solution(price, money, count) {
    var k = 0;
    for(var i=1; i<=count; i++){
        k += i;
    }
    var result = (price*k) - money;
    if(result < 0) return 0
    else return result;
}