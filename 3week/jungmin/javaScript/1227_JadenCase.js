function solution(s) {
    var a = s.split(" ");
    var b = a.map(str=>str.charAt(0).toUpperCase() + str.slice(1).toLowerCase())
    return b.join(" ")
}

// 풀이에 실패해서 구글링한 결과로 작성한 답안입니다.

// charAt(n) : n번째 인덱스의 글자 반환
// slice(a, b) : a번째 인덱스로부터 b개 선택. b생략시 배열 마지막 요소까지 선택.