#!/usr/bin/node

function add(a, b) {
  return (a + b);
}
let num1 = Number(process.argv[2]);
let num2 = Number(process.argv[3]);
let result = add(num1, num2);
console.log(result);
