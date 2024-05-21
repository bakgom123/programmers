function solution(n) {
  const myArray = n.toString().split("").map(Number);
  var sum = myArray.reduce((accumulator, currentValue) => {
    return accumulator + currentValue;
  }, 0);

  return sum;
}
