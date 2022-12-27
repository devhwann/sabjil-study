// 프로그래머스 Level 1 1227_핸드폰 번호 가리기
// https://school.programmers.co.kr/learn/courses/30/lessons/12932

function solution(phone_number) {
  let regex = /[0-9]/; //0 ~9 숫자 정규식

  let toNumber = phone_number.split("").map(Number).join(""); // 숫자로 변환
  let result = "";

  for (i = 0; i < toNumber.length - 4; i++) {
    result += toNumber[i].replace(regex, "*");
  }

  return (result += phone_number.slice(-4));
}
