function solution(s) {
    var result = s.split(" ");
    var answer = [];
    for(var i=0; i<result.length; i++){
        var arr = "";
        for(var j=0; j<result[i].length; j++){
            if(j % 2 === 0){
                arr += result[i][j].toUpperCase();
            } else {
                arr += result[i][j].toLowerCase();
            }
        }
        answer.push(arr);
    }
    return answer.join(" ");
}