function solution(s) {
  var answer = [];

  let result = s.split(" ");

  // for (i = 0; i < result.length; i++) {
  for (i in result) {
    let sum = "";
    // for (j = 0; j < result[i].length; j++) {
    for (j in result[i]) {
      if (j % 2 == 0) {
        sum += result[i][j].toUpperCase(); // i = 0 0번째의 i배열의 j루프
      } else {
        sum += result[i][j].toLowerCase();
      }
    }
    answer.push(sum);
  }

  return answer.join(" ");
}
