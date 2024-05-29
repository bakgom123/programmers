function solution(phone_book) {
  const set = new Set(phone_book);
  return !phone_book.some((str) => {
    for (let i = 1; i < str.length; i++) {
      if (set.has(str.slice(0, i))) {
        return true;
      }
    }
    return false;
  });
}
