function solution(sizes) {
    var arr = [];
    var arr2 = [];
    for(let i=0; i<sizes.length; i++){
        arr.push(sizes[i].sort((a,b)=>b-a).shift());
        arr2.push(sizes[i].shift());
    }
    return arr.sort((a,b)=>b-a)[0] * arr2.sort((a,b)=>b-a)[0];
}