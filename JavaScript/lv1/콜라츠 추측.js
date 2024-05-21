function solution(n) {
  let result = 0;

  while (n !== 1) {
    if (n % 2 === 0) {
      n /= 2;
      result++;
    } else {
      n = 3 * n + 1;
      result++;
    }
  }

  if (result > 500) {
    return -1;
  } else {
    return result;
  }
}
