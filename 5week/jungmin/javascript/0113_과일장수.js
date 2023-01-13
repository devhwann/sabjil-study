function solution(k, m, score) {
    const arr = score.sort((a,b)=>b-a); 
    const ch = Math.floor(arr.length / m); 
    let cnt = 0;
    for(let i=0; i<ch; i++){
        cnt += arr[m*i+m-1] * m;
    }
    return cnt;
}