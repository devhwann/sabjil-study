// 프로그래머스 Level 월간 코드 챌린지 시즌1 3진법 뒤집기
// https://school.programmers.co.kr/learn/courses/30/lessons/68935

function solution(n) {
  // toString은 문자열로 변환 할 때 사용하지만 숫자를 넣으면 진법으로도 사용 가능
  // 배열로 만들어 뒤집고 문자열로 만들어 parseint의 radix 옵션을 사용.  정수로 변환하여 리턴
  return parseInt(n.toString(3).split("").reverse().join(""), 3);
}
