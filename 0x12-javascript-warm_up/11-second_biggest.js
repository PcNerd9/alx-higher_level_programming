#!/usr/bin/node

let max = 0;
let secondMax = 0;
let value;

for (let i = 2; i < process.argv.length; i++) {
  value = parseInt(process.argv[i]);
  if (value) {
    if (value > max) {
      secondMax = max;
      max = value;
    }
  }
}
console.log(secondMax);
