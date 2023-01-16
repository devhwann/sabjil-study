function solution(lottos, win_nums) {
    const arr = [...lottos, ...win_nums].sort((a,b)=>a-b);
    const zero = arr.filter(e => e == 0).length;
    arr.splice(0, zero);
    let cnt = 0;
    for (let i=0; i<arr.length; i++) {
        if(arr[i] == arr[i+1]) {
            cnt++;
        }
    }
    const max = cnt === 0 && zero === 0 ? 6 - cnt - zero : 7 - cnt - zero;
    const min = cnt === 0 ? 6 - cnt : 7 - cnt;
    return [max, min];
}