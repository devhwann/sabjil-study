function solution(array) {
    
    let arr_max = Math.max(...array);
    let idx = array.indexOf(arr_max);
    
    return [arr_max, idx];    
}