function solution(left, right) {
  let result = 0;

  for (let num = left; num <= right; num++) {
    let divisorCount = 0;
    for (let i = 1; i <= num; i++) {
      if (num % i === 0) {
        divisorCount++;
      }
    }

    if (divisorCount % 2 === 0) {
      result += num;
    } else {
      result -= num;
    }
  }

  return result;
}
