// 프로그래머스 Level 1 jihwan: 0103_모스부호
// https://school.programmers.co.kr/learn/courses/30/lessons/120838

function solution(letter) {
  var answer = "";
  let morse = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
  };
  let arr = letter.split(" ");

  for (j in arr) {
    for (i in morse) {
      if (arr[j] == i) {
        answer += morse[i];
      }
    }
  }

  return answer;
}
