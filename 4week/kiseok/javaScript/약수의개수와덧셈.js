function findNum(n){
    let cnt=0;
    for (let i=0; i<=n ; i++){
        if (n%i==0) cnt+=1;
    }
    return cnt;
}

function solution(left, right) {
    var answer = 0;
    for (let i = left; i<=right; i++)
        if(findNum(i)%2==0) answer+=i
        else answer-=i
    return answer;
}