function solution(s) {
    var arr = s.split(" ").sort((a,b)=>{return a-b})
    var arrInt = []
    for(i of arr){
        arrInt.push(parseInt(i))
    }
    var result = [Math.min(...arrInt), Math.max(...arrInt)].join(" ");
    return `${result}`
}