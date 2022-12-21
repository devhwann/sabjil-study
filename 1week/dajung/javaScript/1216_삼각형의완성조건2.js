function solution(sides) {
    let arr1 = [];
    let arr2 = [];
    //가장 긴 변이 포함돼있는 경우
    sides.sort(function (a, b){return a - b;});
    for(let i=sides[1]-sides[0]+1; i<=sides[1]; i++){
        arr1.push(i);
    } 
    //가장 긴 변이 포함되지 않은 경우
    for(let j=sides[0]+sides[1]-1; j>sides[1]; j--){
        arr2.push(j);
    }
    return arr1.length + arr2.length;
}
