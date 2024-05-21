function solution(arr) {
  const min = Math.min(...arr);
  const index = arr.indexOf(min);
  arr.splice(index, 1);

  if (arr.length === 0) {
    return [-1];
  } else {
    return arr;
  }
}
