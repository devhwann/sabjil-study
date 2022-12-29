// 프로그래머스 Level 2 1227_제이든케이스 문자열 만들기
// https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=javascript

function solution(s) {
  let result = "";

  for (i in s) {
    if (s[i - 1] == " " || i == 0)
      // 순회하면서 s의 -1 인덱스가 공백이라면.. 대문자 변환,
      result += s[i].toUpperCase();
    else result += s[i].toLowerCase();
  }

  return result;
}
