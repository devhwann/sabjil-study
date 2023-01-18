function solution(n) {
    const prime = num => {
    for (let i=2; i<= Math.sqrt(num); i++) {
      if (num % i === 0) return true;
    }
    return false;
  };

  let count = 0;

  for (let i=1; i <= n; i++) {
    if (prime(i)) count += 1;
  }
  return count;
}