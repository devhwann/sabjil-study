function solution(numlist, n) {
    var arr = numlist.sort((a,b) => {
        if(Math.abs(a-n) - Math.abs(b-n) == 0){
            return b-a
        }
        return Math.abs(a-n) - Math.abs(b-n)
    });
    return arr
}