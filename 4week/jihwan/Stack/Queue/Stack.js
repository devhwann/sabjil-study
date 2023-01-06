class Stack {
  // 스택 클래스 선언
  constructor() {
    this.arr = []; // 생성자 함수 선언 빈 스택
  }
  push(item) {
    this.arr.push(item); // 삽입
  }
  pop() {
    return this.arr.pop(); // 삭제
  }
  pointer() {
    return `Pointer :${this.arr[this.arr.length - 1]}`; // head의 위치 반환
  }
}

const stack = new Stack();
stack.push(1); // 1삽입
stack.push(2); // 2삽입
stack.push(3); // 3삽입
stack.pop(); // 3삭제
console.log(stack); // 1, 2
stack.push(4); // 4삽입
console.log(stack); // 1, 2 , 4
console.log(stack.pointer()); //  4를 가리키는 포인터
