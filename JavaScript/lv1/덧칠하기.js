// 처음 생각 방식
// function solution(n, m, section) {
//     let ans = 0
//     let start = 0
//     for (let i = 0; i <= n; i++) {
//         if (section[section.length - 1] - section[start] + 1 > m) {
//             start = section[start] + m;
//             ans++;
//         }
//         return ans
//     }
//     return 1;
// }

function solution(n, m, section) {
  let ans = 0;
  let start = 0;

  while (start < section.length) {
    let end = section[start] + m - 1;
    ans++;

    while (start < section.length && section[start] <= end) {
      start++;
    }
  }

  return ans;
}
