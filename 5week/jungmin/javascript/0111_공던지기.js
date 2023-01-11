function solution(numbers, k) {
    let a = 0;
    for(let i = 0; i < k; i++){
        a += 2;    
        if(a > numbers.length){
            a -= numbers.length;
        }
    }
    return numbers[a - 2];
}