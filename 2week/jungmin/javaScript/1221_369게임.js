function solution(order) {
    let arr = String(order).split("");
    let cnt = 0;
    for(i of arr) {
        if(i != 0 && i % 3 === 0) cnt++;
    }
    return cnt
}