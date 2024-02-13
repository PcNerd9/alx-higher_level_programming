#!/usr/bin/node

let number = 0;
let biggest = 0;
let secondBiggest = 0;
const lenght = process.argv.length;
if (lenght === 2) {
  console.log(0);
} else {
  for (let i = 2; i < lenght; i++) {
    number = Number(process.argv[i]);
    if (number > biggest) {
      secondBiggest = biggest;
      biggest = number;
    }
  }
}
console.log(secondBiggest);
