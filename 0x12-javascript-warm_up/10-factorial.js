#!/usr/bin/node

const number = Number(process.argv[2]);
function factorial (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n <= 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}
const result = factorial(number);
console.log(result);
