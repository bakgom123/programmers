function solution(n) {
  const myArray = n.toString().split("").map(Number);
  const des = myArray.sort((a, b) => b - a);
  console.log(des);

  return Number(des.join(""));
}
