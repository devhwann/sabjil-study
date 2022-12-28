function solution(array, commands) {
    var arr = [];
    for(var i=0; i<commands.length; i++){
        var a = commands[i][0];
        var b = commands[i][1];
        var c = commands[i][2];
        var arr2 = array.slice(a-1, b).sort((n,m)=>n-m)
        arr.push(arr2[c-1]);
    }
    return arr
}