function solution(n) {
  const countOnes = (num) => num.toString(2).split("1").length - 1;
  const targetOnes = countOnes(n);
  let res = n + 1;

  while (true) {
    if (countOnes(res) === targetOnes) {
      return res;
    } else {
      res += 1;
    }
  }
}
