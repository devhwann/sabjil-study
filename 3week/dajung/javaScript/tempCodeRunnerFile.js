
function solution(s) {
    return s.toLowerCase().split("").reduce((sum, c, idx)=>{
        if ((s[idx-1] === " " && c !== " ") || s.indexOf(c) === 0)//단어의 첫 문자일 조건
            return sum += c.toUpperCase()
        return sum += c
    }, "")
}