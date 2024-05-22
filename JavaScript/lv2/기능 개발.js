function solution(progresses, speeds) {
  let answer = [];
  //   ceil - 2.3일이 걸린다면 3일로 계산
  let days_need = progresses.map((progress, index) =>
    Math.ceil((100 - progress) / speeds[index])
  );

  let max_days = days_need[0];
  let count = 0;

  for (let days of days_need) {
    if (days <= max_days) {
      count++;
    } else {
      answer.push(count);
      count = 1;
      max_days = days;
    }
  }

  answer.push(count);

  return answer;
}
