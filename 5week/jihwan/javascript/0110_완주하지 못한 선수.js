// 프로그래머스 Level 1 완주하지 못한 선수
//  https://school.programmers.co.kr/learn/courses/30/lessons/42576

function solution(participant, completion) {
  completion.sort();
  participant.sort();

  for (i in participant) {
    console.log(participant[i]);
    console.log(completion[i]);
    if (participant[i] !== completion[i]) {
      return participant[i];
    }
    //  filter로 간단히 구현해보려 했으나 ..
    //     if(!participant.filter(x => !completion.includes(x))) {
    //         // if()
    //         // return participant.filter((v, i) => participant.indexOf(v) === i); //
    //     } else {
    //         return participant.filter(x => !completion.includes(x)).join('')
    //     }
  }
}
