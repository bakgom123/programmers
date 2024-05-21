function solution(phone_number) {
  let answer = "*".repeat(phone_number.length - 4);
  return answer + phone_number.substring(phone_number.length - 4);
}
