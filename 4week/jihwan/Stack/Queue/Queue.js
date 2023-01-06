class Queue {
  // 클래스 선언
  constructor() {
    // 생성자 함수 선언
    this.arr = [];
  }
  enqueue(item) {
    //삽입
    this.arr.push(item);
  }
  dequeue() {
    //삭제
    return this.arr.shift();
  }
}

const queue = new Queue();
queue.enqueue(1); // 1삽입
queue.enqueue(2); // 2삽입
queue.enqueue(3); // 3삽입
queue.dequeue(); // 1

console.log(queue); // 2 , 3
