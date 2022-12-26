// 프로그래머스 Level 1 1226_서울에서 김서방 찾기
// https://school.programmers.co.kr/learn/courses/30/lessons/12919

function solution(seoul) {
  let findArr = seoul.lastIndexOf("Kim");

  return `김서방은 ${findArr}에 있다`;
}
