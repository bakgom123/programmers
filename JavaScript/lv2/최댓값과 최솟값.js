function solution(s) {
  const numbers = s.split(" ").map((num) => parseInt(num));

  const min = Math.min(...numbers);
  const max = Math.max(...numbers);

  return `${min} ${max}`;
}
