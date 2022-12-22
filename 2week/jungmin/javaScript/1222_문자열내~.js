function solution(s){
    let arr = s.split("");
    var p_cnt = 0;
    var y_cnt = 0;
    for(i of arr){
        if(i === "p" || i === "P"){
            p_cnt++;
        } else if(i === "y" || i === "Y") {
            y_cnt++;
        }
    }
    return p_cnt === y_cnt
}